# -*- coding: utf-8 -*-
"""C++ code generation

This module uses the clang compiler to generate setter/getter for each
parameter with "parameter_t" type.

"clang" parse the "input.h" file to find all the parameter_t type.

Example:

        ::

        $ python test2.py    ./pycparser/tests/c_files/zipLoad.h

"""
import os
import sys
import clang.cindex

from collections import OrderedDict

COPYRIGHT = \
    """/*
 * LLNS Copyright Start
 * Copyright (c) 2017, Lawrence Livermore National Security
 * This work was performed under the auspices of the U.S. Department
 * of Energy by Lawrence Livermore National Laboratory in part under
 * Contract W-7405-Eng-48 and in part under Contract DE-AC52-07NA27344.
 * Produced at the Lawrence Livermore National Laboratory.
 * All rights reserved.
 * For details, see the LICENSE file.
 * LLNS Copyright End
 */

 /*  This code has been automatically generated. */
"""

tabsize = 4
AUTOGEN = '--AUTOGEN--'

GET_CUSTOM = 'AUTOGEN_GET_WITH_CUSTOM'
SET_CUSTOM = 'AUTOGEN_SET_WITH_CUSTOM'
GET_SET_CUSTOM = 'AUTOGEN_GET_SET_CUSTOM'

GET_STRING_CUSTOM = 'AUTOGEN_GET_STRING_WITH_CUSTOM'
SET_STRING_CUSTOM = 'AUTOGEN_SET_STRING_WITH_CUSTOM'

GET_FLAG_CUSTOM = 'AUTOGEN_GET_FLAG_WITH_CUSTOM'
SET_FLAG_CUSTOM = 'AUTOGEN_SET_FLAG_WITH_CUSTOM'

GET = 'AUTOGEN_GET'
SET = 'AUTOGEN_SET'
GET_SET = 'AUTOGEN_GET_SET'

GET_STRING = 'AUTOGEN_GET_STRING'
SET_STRING = 'AUTOGEN_SET_STRING'

GET_FLAG = 'AUTOGEN_GET_FLAG'
SET_FLAG = 'AUTOGEN_SET_FLAG'
ALL_FLAGS = 'AUTOGEN_FLAGS'

GET_PSTRING = 'AUTOGEN_GET_PSTRING'

getFunction = "double {}::get(const string &param, units_t unitType) const"
setFunction = "void {}::set(const string &param, double val, units_t unitType)"
getString = "string getString (const string & param) const"
getParamString = "void getConfigurableSpec (stringVec & pstr, paramStringType pstype) const"


class Parse:

    def __init__(self):
        """
        Intialize global variable.
        """
        self.currentClass = ""
        self.tab = 0
        self.namespaceList = []
        self.parentClass = {}
        self.allClass = []
        self.autogen = {}
        self.autogen.update({"HasMacro": False})  # Set to true if any macro is defined in header file.

    def dump_children(self, node, fn):
        """
        Arguments:
            node {cland.index} -- [clang cursor]
            fn {string} -- [filename]
        """

        for c in node.get_children():
            filename = str(c.location)
            # if(filename.find("griddyn_autogen") != -1):
            # print c.location
            # print c.displayname, c.kind, c.spelling, c.type.spelling
            # print "Data %s" % (c.data)
            if(str(c.location).find(str(fn)) != -1):
                #
                # we can read a line directly in the source file.includes
                #
                filename = c.location.file.name
                with open(filename, 'r') as fh:
                    contents = fh.read()
                # print c.kind, c.spelling, c.type.spelling, c.access_specifier
                # if c.kic.kinnd == clang.cindex.CursorKind.FIELD_DECL and
                # (c.type.spelling.find('parameter_t') != -1):
                if c.kind == clang.cindex.CursorKind.NAMESPACE:
                    self.namespaceList.append(c.spelling)

                if c.kind == clang.cindex.CursorKind.CLASS_DECL:
                    self.autogen.update(OrderedDict(
                        {c.spelling: {'Parameters': OrderedDict(),  # Parameter_t for Get and Set
                                      'StringParam': OrderedDict(),
                                      'AliasParam': OrderedDict(),
                                      'AliasFlags': OrderedDict(),
                                      'AliasString': OrderedDict(),
                                      'Flags': OrderedDict(),
                                      'SetStringCustomParam': OrderedDict(),
                                      'GetStringCustomParam': OrderedDict(),
                                      'GetCustomParam': OrderedDict(),
                                      'SetCustomParam': OrderedDict(),
                                      'SetFlagCustomParam': OrderedDict(),
                                      'GetFlagCustomParam': OrderedDict(),
                                      'NeedIncludeSet': False,
                                      'HasGetCustomParam': False,
                                      'HasSetCustomParam': False,
                                      'HasGetFlagCustomParam': False,
                                      'HasSetFlagCustomParam': False,
                                      'HasGetStringCustomParam': False,
                                      'HasSetStringCustomParam': False,
                                      'HasParameterString': False,
                                      'HasSet': False,
                                      'HasGet': False,
                                      'HasSetFlag': False,
                                      'HasGetFlag': False,
                                      'HasSetString': False,
                                      'HasGetString': False}
                         }))

                    self.parentClass[c.spelling] = []
                    for child in c.get_children():
                        if child.kind == clang.cindex.CursorKind.CXX_BASE_SPECIFIER:
                            self.parentClass[c.spelling].append(child.get_definition().displayname)
                    self.allClass.append(c.spelling)
                    self.currentClass = c.spelling

                #
                # Extract information when METHOD Declaration Macro are found in .h class file.
                #
                if(c.kind == clang.cindex.CursorKind.CXX_METHOD) and self.currentClass != '':
                    declaration = contents[c.extent.start.offset:c.extent.end.offset]
                    autogen = self.autogen[self.currentClass]
                    if declaration == GET:
                        autogen['HasGet'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == SET:
                        autogen['HasSet'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == GET_SET:
                        autogen['HasGet'] = True
                        autogen['HasSet'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == GET_STRING:
                        autogen['HasGetString'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == SET_STRING:
                        autogen['HasSetString'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == SET_FLAG:
                        autogen['HasSetFlag'] = True
                        self. autogen['HasMacro'] = True

                    elif declaration == GET_FLAG:
                        autogen['HasGetFlag'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == ALL_FLAGS:
                        autogen['HasGetFlag'] = True
                        autogen['HasSetFlag'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == GET_CUSTOM:
                        autogen['NeedIncludeSet'] = True
                        autogen['HasGet'] = True
                        autogen['HasGetCustomParam'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == SET_CUSTOM:
                        autogen['NeedIncludeSet'] = True
                        autogen['HasSet'] = True
                        autogen['HasSetCustomParam'] = True
                        self. autogen['HasMacro'] = True

                    elif declaration == GET_SET_CUSTOM:
                        autogen['NeedIncludeSet'] = True
                        autogen['HasGet'] = True
                        autogen['HasSet'] = True
                        autogen['HasGetCustomParam'] = True
                        autogen['HasSetCustomParam'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == GET_STRING_CUSTOM:
                        autogen['NeedIncludeSet'] = True
                        autogen['HasGetString'] = True
                        self.autogen['HasGetStringCustomParam'] = True

                    elif declaration == SET_STRING_CUSTOM:
                        autogen['NeedIncludeSet'] = True
                        autogen['HasSetString'] = True
                        autogen['HasSetStringCustomParam'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == SET_FLAG_CUSTOM:
                        autogen['NeedIncludeSet'] = True
                        autogen['HasSetFlag'] = True
                        autogen['HasSetFlagCustomParam'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == GET_FLAG_CUSTOM:
                        autogen['NeedIncludeSet'] = True
                        autogen['HasGetFlag'] = True
                        autogen['HasGetFlagCustomParam'] = True
                        self.autogen['HasMacro'] = True

                    elif declaration == GET_PSTRING:
                        autogen['HasParameterString'] = True
                        self.autogen['HasMacro'] = True
                #
                # Extract information from CLASS Comment block
                # The comment block does not triggered the function, but the macro declaration does.
                #
                if(c.kind == clang.cindex.CursorKind.CXX_ACCESS_SPEC_DECL and
                        c.brief_comment is not None):
                    if(c.brief_comment.find(AUTOGEN) != -1):
                        # print "brief", c.brief_comment, c.kind

                        GetCustomParam = self.autogen[self.currentClass]['GetCustomParam']
                        SetCustomParam = self.autogen[self.currentClass]['SetCustomParam']
                        SetStringParam = self.autogen[self.currentClass]['SetStringCustomParam']
                        GetStringParam = self.autogen[self.currentClass]['GetStringCustomParam']
                        SetFlagsParam = self.autogen[self.currentClass]['SetFlagCustomParam']
                        GetFlagsParam = self.autogen[self.currentClass]['GetFlagCustomParam']

                        Comment = c.raw_comment.split('\n')
                        for i in range(len(Comment)):
                            if Comment[i].find('GET_CUSTOM') != -1:
                                param = Comment[i].split(':')[1:][0].split()
                                for j in range(len(param)):
                                    GetCustomParam.update(OrderedDict({j: param[j]}))
                            if Comment[i].find('SET_CUSTOM') != -1:
                                param = Comment[i].split(':')[1:][0].split()
                                for j in range(len(param)):
                                    SetCustomParam.update(OrderedDict({j: param[j]}))
                            if Comment[i].find('GET_FLAG') != -1:
                                param = Comment[i].split(':')[1:][0].split()
                                for j in range(len(param)):
                                    GetFlagsParam.update(OrderedDict({j: param[j]}))
                            if Comment[i].find('SET_FLAG') != -1:
                                param = Comment[i].split(':')[1:][0].split()
                                for j in range(len(param)):
                                    SetFlagsParam.update(OrderedDict({j: param[j]}))
                            if Comment[i].find('GET_STRING') != -1:
                                param = Comment[i].split(':')[1:][0].split()
                                for j in range(len(param)):
                                    GetStringParam.update(OrderedDict({j: param[j]}))
                            if Comment[i].find('SET_STRING') != -1:
                                param = Comment[i].split(':')[1:][0].split()
                                for j in range(len(param)):
                                    SetStringParam.update(OrderedDict({j: param[j]}))

                # print c.kind, c.spelling, c.raw_comment, c.location
                # print c.referenced.access_specifier
                #
                # Do not extract PROTECTED parameter_t
                #
                # if c.referenced is not None and c.referenced.access_specifier.name == 'PROTECTED':
                #    continue
                # ---------------------------------
                # enum must be attached to a class
                # ---------------------------------
                if c.kind == clang.cindex.CursorKind.ENUM_CONSTANT_DECL and(
                        c.type.spelling.find('flags') != -1) and \
                        self.currentClass != '':
                    Flags = self.autogen[self.currentClass]['Flags']
                    Aliases = self.autogen[self.currentClass]['AliasFlags']
                    if c.raw_comment is not None and c.raw_comment.find("{") != -1:
                        begin = c.raw_comment.find("{") + 1
                        end = c.raw_comment.find("}")
                        Aliases.update(
                            OrderedDict({c.displayname: c.raw_comment[begin: end]})
                        )
                    Flags.update(OrderedDict({c.displayname: c.type.spelling}))
                    pass

                if c.kind == clang.cindex.CursorKind.FIELD_DECL and (
                        c.type.spelling.find('parameter_t') != -1):
                    # print c.referenced.access_specifier.name
                    key = c.spelling.upper()
                    Parameters = self.autogen[self.currentClass]['Parameters']
                    StringParam = self.autogen[self.currentClass]['StringParam']
                    Aliases = self.autogen[self.currentClass]['AliasParam']
                    StringParam.update(OrderedDict({key: c.spelling}))
                    try:
                        # print c.raw_comment
                        if c.raw_comment.find("[") != -1:
                            # print c.raw_comment
                            begin = c.raw_comment.find("[") + 1
                            end = c.raw_comment.find("]")
                            template = "unitConversion ({}, {}, unitType, systemBasePower)".format(
                                "{}", c.raw_comment[begin:end])
                            Parameters.update(OrderedDict({key: template}))
                        else:
                            Parameters.update(OrderedDict({key: c.spelling}))

                        if c.raw_comment.find("{") != -1:
                            begin = c.raw_comment.find("{") + 1
                            end = c.raw_comment.find("}")
                            Aliases.update(
                                OrderedDict({key: c.raw_comment[begin: end]})
                            )

                    except BaseException:
                        Parameters.update(OrderedDict({key: c.spelling}))
            self.dump_children(c, fn)
        return self.namespaceList, self.autogen, self.allClass, self.parentClass


class createFile:

    def __init__(self):
        self.tab = 0

    def printHeader(self, namespace, autogen, allClass):
        """ Print header file

        Arguments:
            namespaceList {list} -- list of namespace to use
            paramListKey {all parameters} -- create enumeration class
        """
        tab = self.tab
        print COPYRIGHT
        print tab * " ", '#include "' + allClass[0] + '.h"'
        print tab * " ", '#include "core/coreObjectTemplates.hpp"'
        print tab * " ", '#include <map>'
        custom = False
        namespaceStringVec = False
        for cl in allClass:
            CustomParam = autogen[cl]['NeedIncludeSet']
            StringVec = autogen[cl]['HasParameterString']
            if CustomParam:
                custom = True
            if StringVec:
                namespaceStringVec = True

        if custom:
            print tab * " ", "#include <set>"

        print
        print tab * " ", 'using namespace std;'
        print tab * " ", 'using namespace gridUnits;'
        print tab * " ", 'using namespace ' + "::".join(namespace) + ";"

        if namespaceStringVec:
            print tab * " ", 'using griddyn::stringVec;'

        print
        #
        # create enum class
        for i in range(len(allClass)):
            parameters = autogen[allClass[i]]['Parameters']
            HasSet = autogen[allClass[i]]['HasSet']
            HasGet = autogen[allClass[i]]['HasGet']
            if HasSet or HasGet:
                if len(parameters) != 0:
                    print tab * " ", "enum class " + allClass[i] + "Params { ",
                    for param in parameters.keys():
                        print param + ",",
                    print"};"
                print

        #
        # create map pairs.
        #
        allcustomLocNum = []
        allcustomLocFlags = []
        allcustomLocString = []
        if custom:
            for i in range(len(allClass)):
                autogenCl = autogen[allClass[i]]
                HasGetCustomParam = autogenCl['HasGetCustomParam']
                HasSetCustomParam = autogenCl['HasSetCustomParam']
                HasSetStringParam = autogenCl['HasSetStringCustomParam']
                HasGetStringParam = autogenCl['HasGetStringCustomParam']
                HasSetCustomFlags = autogenCl['HasSetFlagCustomParam']
                HasGetCustomFlags = autogenCl['HasGetFlagCustomParam']

                if(HasGetCustomParam):
                    GetCustomParam = autogen[allClass[i]]['GetCustomParam']
                    if(len(GetCustomParam) > 0):
                        print tab * " ", "static const set<string> ",
                        print "CustomParamGet" + allClass[i] + "{",
                        for (j, param) in enumerate(GetCustomParam.keys()):
                            allcustomLocNum.append(GetCustomParam[param].replace('"', '').replace(',', ''))
                            print GetCustomParam[param],
                        print "};"

                if(HasSetCustomParam):
                    SetCustomParam = autogen[allClass[i]]['SetCustomParam']
                    if(len(SetCustomParam) > 0):
                        print tab * " ", "static const set<string> ",
                        print "CustomParamSet" + allClass[i] + "{",
                        for (j, param) in enumerate(SetCustomParam.keys()):
                            allcustomLocNum.append(SetCustomParam[param].replace('"', '').replace(',', ''))
                            print SetCustomParam[param],
                        print "};"

                if(HasGetCustomFlags):
                    GetFlagCustomParam = autogen[allClass[i]]['GetFlagCustomParam']
                    if(len(GetFlagCustomParam) > 0):
                        print tab * " ", "static const set<string> ",
                        print "CustomFlagGet" + allClass[i] + "{",
                        for (j, param) in enumerate(GetFlagCustomParam.keys()):
                            allcustomLocFlags.append(GetFlagCustomParam[param].replace('"', '').replace(',', ''))
                            print GetFlagCustomParam[param],
                        print "};"

                if(HasSetCustomFlags):
                    SetFlagCustomParam = autogen[allClass[i]]['SetFlagCustomParam']
                    if(len(SetFlagCustomParam) > 0):
                        print tab * " ", "static const set<string> ",
                        print "CustomFlagSet" + allClass[i] + "{",
                        for (j, param) in enumerate(SetFlagCustomParam.keys()):
                            allcustomLocFlags.append(SetFlagCustomParam[param].replace('"', '').replace(',', ''))
                            print SetFlagCustomParam[param],
                        print "};"

                if(HasGetStringParam):
                    GetStringCustomParam = autogen[allClass[i]]['GetStringCustomParam']
                    if(len(GetStringCustomParam) > 0):
                        print tab * " ", "static const set<string> ",
                        print "CustomParamGetString" + allClass[i] + "{",
                        for (j, param) in enumerate(GetStringCustomParam.keys()):
                            allcustomLocString.append(GetStringCustomParam[param].replace('"', '').replace(',', ''))
                            print GetStringCustomParam[param],
                        print "};"

                if(HasSetStringParam):
                    SetStringCustomParam = autogen[allClass[i]]['SetStringCustomParam']
                    if(len(SetStringCustomParam) > 0):
                        print tab * " ", "static const set<string> ",
                        print "CustomParamSetString" + allClass[i] + "{",
                        for (j, param) in enumerate(SetStringCustomParam.keys()):
                            allcustomLocString.append(SetStringCustomParam[param].replace('"', '').replace(',', ''))
                            print SetStringCustomParam[param],
                        print "};"
                print
        for i in range(len(allClass)):
            parameters = autogen[allClass[i]]['Parameters']
            aliases = autogen[allClass[i]]['AliasParam']
            Flags = autogen[allClass[i]]['Flags']
            aliasFlags = autogen[allClass[i]]['AliasFlags']
            stringParam = autogen[allClass[i]]['StringParam']
            HasSet = autogen[allClass[i]]['HasSet']
            HasGet = autogen[allClass[i]]['HasGet']
            HasParameterString = autogen[allClass[i]]['HasParameterString']
            HasSetFlag = autogen[allClass[i]]['HasSetFlag']
            HasGetFlag = autogen[allClass[i]]['HasGetFlag']

            if HasSet or HasGet:
                self.printMapPair("Params", parameters, aliases, allClass[i], True)
            if HasSetFlag or HasGetFlag:
                self.printMapPair("Flags", Flags, aliasFlags, allClass[i], False)
            if HasParameterString:
                self.printLocalParam("allowedNumericalParameters", parameters, allcustomLocNum, aliases, allClass[i])
                self.printLocalParam("allowedFlags", Flags, allcustomLocFlags, aliasFlags, allClass[i])
                self.printLocalParam("allowedStringParameters", stringParam,  allcustomLocString, {}, allClass[i])

        print
        for ns in namespace:
            print tab * " ",
            print "namespace {} ".format(ns), "{ "
            tab = tab + tabsize

        self.tab = tab

    def printLocalParam(self, name, paramList, customList, aliases, griddynClass):
        """
        """
        tab = self.tab

        if(len(paramList.keys()) != 0) or (len(customList) != 0):
            print tab * " ", "static const stringVec " + name + griddynClass + "{",
            for i, param in enumerate(customList):
                print "\"" + param.lower() + "\",",
                if(i % 5) == 0 and i != 0:
                    print
                    print 38 * " ",
            for i, param in enumerate(paramList.keys()):
                if(param in aliases.keys()):
                    for alias in aliases[param].split(','):
                        print "\"" + alias.replace('"', '').lower().strip() + "\",",
                if(i != len(paramList) - 1):
                    print "\"" + param.lower() + "\",",
                else:
                    print "\"" + param.lower() + "\" };"
                if(i % 5) == 0 and i != 0:
                    print
                    print 38 * " ",
            if(len(paramList.keys()) == 0) and (len(customList) != 0):
                print "};"

        self.tab = tab

    def printMapPair(self, name, paramList, aliases, griddynClass, local):
        """CreateMap  parameter list.

        Arguments:
            paramList {list of parameters} -- create map pairs.
        """
        tab = self.tab
        mapName = name + "Map" + griddynClass
        if local:
            enumType = griddynClass + name
        else:
            enumType = "int"

        if(len(paramList) == 0):
            print tab * " "
            print tab * " ", "static const map<string, " + enumType + "> " + mapName + "{};"

        if(len(paramList) != 0):

            print tab * " "
            print tab * " ", "static const map<string, " + enumType + "> " + mapName + "{"

            for i, param in enumerate(paramList.keys()):
                if local:
                    value = griddynClass + name + "::" + param.upper()
                else:
                    value = paramList[param].split("::")[-2] + "::" + param

                if(param in aliases.keys()):
                    for alias in aliases[param].split(','):
                        print tab * " ", "{\"" + alias.replace('"', '').lower().strip() + "\", " + value + "},"
                if(i != len(paramList) - 1):
                    print tab * " ", "{\"" + param.lower() + "\", " + value + "},"
                else:
                    print tab * " ", "{\"" + param.lower() + "\", " + value + "}"
            print tab * " ", "};"
        self.tab = tab

    def printSetFunction(self, autogen, allClass, parentClass):
        """

        Arguments:
            paramList {list} -- parameter list
            setFunction {string} -- set method declaratioin
        """
        tab = self.tab

        for i in range(len(allClass)):
            curClass = allClass[i]
            HasSet = autogen[curClass]['HasSet']
            if HasSet:

                Parameters = autogen[curClass]['Parameters']
                stringKeys = autogen[curClass]['StringParam'].keys()
                stringParam = autogen[curClass]['StringParam']
                HasSetCustomParam = autogen[curClass]['HasSetCustomParam']
                mapName = "ParamsMap" + curClass

                if(HasSetCustomParam):
                    print tab * " ", "void " + curClass + "::custom_set(const string &param, double val, units_t unitType)"
                    print tab * " ", "{"
                    print tab * " ", "    return;"
                    print tab * " ", "}"
                    print tab * " ", "/* Is this a custom parameter? */"
                    print tab * " ", "static bool " + curClass + "CustomSetCheck(const string & param)"
                    print tab * " ", "{"
                    tab = tab + tabsize
                    print tab * " ", "return CustomParamSet" + curClass + ".find(param) != CustomParamSet" + curClass + ".end();"
                    tab = tab - tabsize
                    print tab * " ", "}"

                print tab * " ", setFunction.format(curClass)
                print tab * " ", "{"
                tab = tab + tabsize
                #
                # Need to return custom parameter if it is in tthe Set
                #
                if(HasSetCustomParam):
                    print tab * " ", "if(" + curClass + "CustomSetCheck(param))"
                    print tab * " ", "{"
                    tab = tab + tabsize
                    print tab * " ", "return custom_set(param, val, unitType);"
                    tab = tab - tabsize
                    print tab * " ", "}"

                print tab * " ", "auto it = " + mapName + ".find(param);"
                print
                print tab * " ", "if(it==" + mapName + ".end())"
                print tab * " ", "{"
                print tab * " ", "    " + parentClass[curClass][0] + "::set (param, val, unitType);"
                print tab * " ", "}"
                print tab * " ", "switch (it->second)"
                print tab * " ", "{"
                tab = tab + tabsize
                for (j, param) in enumerate(Parameters.keys()):
                    print tab * " ", "case " + curClass + "Params::" + stringKeys[j].upper() + ":"
                    print tab * " ", "    " + stringParam[param] + " = val;"
                    print tab * " ", "    break;"
                print tab * " ", "default:"
                print tab * " ", "    " + parentClass[curClass][0] + "::set (param, val, unitType);"

                print tab * " ", "    break;"
                tab = tab - tabsize
                print tab * " ", "}"
                tab = tab - tabsize
                print tab * " ", "}"
        self.tab = tab

    def printFooter(self, paramList):
        """
        Arguments:
            paramList {list} -- [list of namespace]
        """
        tab = self.tab
        for i in range(len(paramList)):
            tab = tab - tabsize
            print tab * " ", "}"
        self.tab = tab

    def printGetString(self, autogen, allClass, parentClass):
        """
        """
        tab = self.tab
        for i in range(len(allClass)):
            curClass = allClass[i]
            HasGetCustomString = autogen[curClass]['HasGetStringCustomParam']
            HasGetString = autogen[curClass]['HasGetString']

            if(HasGetCustomString):
                HasGetString = True
                print tab * " ", "string " + curClass + "::custom_get(const string &param) const"
                print tab * " ", "{"
                print tab * " ", "    return \"\";"
                print tab * " ", "}"
                print tab * " ", "/* Is this a custom String? */"
                print tab * " ", "static bool " + curClass + "CustomGetStringCheck(const string &param)"
                print tab * " ", "{"
                tab = tab + tabsize
                print tab * " ", "return CustomParamGetString" + curClass + ".find(param) != CustomParamGetString" + curClass + ".end();"
                tab = tab - tabsize
                print tab * " ", "}"

            if(HasGetString):
                print tab * " ", "string " + curClass + "::getString(const string &param) const"
                print tab * " ", "{"
                tab = tab + tabsize

            if(HasGetCustomString):
                print tab * " ", "if(" + curClass + "CustomGetStringCheck(param))"
                print tab * " ", "{"
                tab = tab + tabsize
                print tab * " ", "return " + curClass + "::custom_get(param);"
                tab = tab - tabsize
                print tab * " ", "}"
                print tab * " ", "else"
                print tab * " ", "{"
                tab = tab + tabsize

            if(HasGetString):
                print tab * " ", "return " + parentClass[curClass][0] + "::getString(param);"

            if(HasGetCustomString):
                tab = tab - tabsize
                print tab * " ", "}"
            if(HasGetString):
                tab = tab - tabsize
                print tab * " ", "}"
            print

    def printSetString(self, autogen, allClass, parentClass):
        """
        """
        tab = self.tab
        for i in range(len(allClass)):
            curClass = allClass[i]
            HasSetString = autogen[curClass]['HasSetString']
            HasSetCustomString = autogen[curClass]['HasSetStringCustomParam']
            if(HasSetString):
                if(HasSetCustomString):
                    print tab * " ", "void " + curClass + "::custom_set(const string &param, const string &val)"
                    print tab * " ", "{"
                    print tab * " ", "    return;"
                    print tab * " ", "}"
                    print tab * " ", "/* Is this a custom String? */"
                    print tab * " ", "static bool " + curClass + "CustomSetStringCheck(const string &param)"
                    print tab * " ", "{"
                    tab = tab + tabsize
                    print tab * " ", "return CustomParamSetString" + curClass + ".find(param) != CustomParamSetString" + curClass + ".end();"
                    tab = tab - tabsize
                    print tab * " ", "}"

                print tab * " ", "void " + curClass + "::set(const string &param, const string &val)"
                print tab * " ", "{"
                tab = tab + tabsize
                if(HasSetCustomString):
                    print tab * " ", "if(" + curClass + "CustomSetStringCheck(param))"
                    print tab * " ", "{"
                    tab = tab + tabsize
                    print tab * " ", curClass + "::custom_set(param, val);"
                    tab = tab - tabsize
                    print tab * " ", "}"
                    print tab * " ", "else"
                    print tab * " ", "{"
                    tab = tab + tabsize
                print tab * " ", parentClass[curClass][0] + "::set(param, val);"

                if(HasSetCustomString):
                    tab = tab - tabsize
                    print tab * " ", "}"
                tab = tab - tabsize
                print tab * " ", "}"
                print

    def printSetFlag(self, autogen, allClass, parentClass):
        """
        """
        tab = self.tab

        for i in range(len(allClass)):
            curClass = allClass[i]
            Flags = autogen[curClass]["Flags"]
            Aliases = autogen[curClass]["AliasFlags"]
            mapName = "FlagsMap" + curClass

            HasSetCustomFlags = autogen[curClass]['HasSetFlagCustomParam']
            HasSetFlag = autogen[curClass]['HasSetFlag']
            if HasSetFlag:
                if(HasSetCustomFlags):
                    print tab * " ", "void " + curClass + "::custom_setFlag(const string &flag, bool val)"
                    print tab * " ", "{"
                    print tab * " ", "    return;"
                    print tab * " ", "}"
                    print tab * " ", "/* Is this a custom flag? */"
                    print tab * " ", "static bool " + curClass + "CustomSetFlagCheck(const string &flag)"
                    print tab * " ", "{"
                    tab = tab + tabsize
                    print tab * " ", "return CustomFlagSet" + curClass + ".find(flag) != CustomFlagSet" + curClass + ".end();"
                    tab = tab - tabsize
                    print tab * " ", "}"

                print tab * " ", "void " + curClass + "::setFlag(const string &flag, bool val)"
                print tab * " ", "{"
                tab = tab + tabsize

                if(HasSetCustomFlags):
                    print tab * " ", "if(" + curClass + "CustomSetFlagCheck(flag))"
                    print tab * " ", "{"
                    tab = tab + tabsize
                    print tab * " ", curClass + "::custom_setFlag(flag, val);"
                    tab = tab - tabsize
                    print tab * " ", "}"

                print tab * " ", "auto it = " + mapName + ".find(flag);"
                print
                print tab * " ", "if(it==" + mapName + ".end())"
                print tab * " ", "{"
                tab = tab + tabsize
                if len(parentClass[curClass]) != 0:
                    print tab * " ", parentClass[curClass][0] + "::setFlag(flag, val);"
                else:
                    print tab * " ", "    return; /* No parent class to " + curClass + "*/"
                tab = tab - tabsize
                print tab * " ", "}"
                print tab * " ", "switch (it->second)"
                print tab * " ", "{"
                tab = tab + tabsize
                for (j, flag) in enumerate(Flags.keys()):
                    print tab * " ", "case " + flag + ": "
                    print tab * " ", "    " + "opFlags.set(" + flag + ", val);"
                    print tab * " ", "    break;"
                print tab * " ", "default:"
                if len(parentClass[curClass]) != 0:
                    print tab * " ", "    " + parentClass[curClass][0] + "::setFlag(flag, val);"
                else:
                    print tab * " ", "    return; /* No parent class to " + curClass + "*/"
                print tab * " ", "    break;"
                tab = tab - tabsize
                print tab * " ", "}"
                tab = tab - tabsize
                print tab * " ", "}"
                print

    def printGetFlag(self, autogen, allClass, parentClass):
        """
        """
        tab = self.tab
        for i in range(len(allClass)):
            curClass = allClass[i]
            Flags = autogen[curClass]["Flags"]
            mapName = "FlagsMap" + curClass

            HasGetCustomFlags = autogen[curClass]['HasGetFlagCustomParam']
            HasGetFlag = autogen[curClass]['HasGetFlag']
            if HasGetFlag:
                if(HasGetCustomFlags):
                    print tab * " ", "bool " + curClass + "::custom_getFlag(const string &flag) const"
                    print tab * " ", "{"
                    print tab * " ", "    return false;"
                    print tab * " ", "}"
                    print tab * " ", "/* Is this a custom flag? */"
                    print tab * " ", "static bool " + curClass + "CustomGetFlagCheck(const string &flag)"
                    print tab * " ", "{"
                    tab = tab + tabsize
                    print tab * " ", "return CustomFlagGet" + curClass + ".find(flag) != CustomFlagGet" + curClass + ".end();"
                    tab = tab - tabsize
                    print tab * " ", "}"

                print tab * " ", "bool " + curClass + "::getFlag(const string &flag) const"
                print tab * " ", "{"
                tab = tab + tabsize
                if(HasGetCustomFlags):
                    print tab * " ", "if(" + curClass + "CustomGetFlagCheck(flag))"
                    print tab * " ", "{"
                    tab = tab + tabsize
                    print tab * " ", "return " + curClass + "::custom_getFlag(flag);"
                    tab = tab - tabsize
                    print tab * " ", "}"

                print tab * " ", "auto it = " + mapName + ".find(flag);"
                print
                print tab * " ", "if(it==" + mapName + ".end())"
                print tab * " ", "{"
                tab = tab + tabsize
                print tab * " ", parentClass[curClass][0] + "::getFlag(flag);"
                tab = tab - tabsize
                print tab * " ", "}"
                print tab * " ", "switch (it->second)"
                print tab * " ", "{"
                tab = tab + tabsize
                for (j, flag) in enumerate(Flags.keys()):
                    print tab * " ", "case " + flag + ": "
                    print tab * " ", "    " + "return opFlags[" + flag + "];"
                    print tab * " ", "    break;"
                print tab * " ", "default:"
                print tab * " ", "    return " + parentClass[curClass][0] + "::getFlag(flag);"
                print tab * " ", "    break;"
                tab = tab - tabsize
                print tab * " ", "}"
                tab = tab - tabsize
                print tab * " ", "}"
                print

    def printGetFunction(self, autogen, allClass, parentClass):
        """
        """
        tab = self.tab
        for i in range(len(allClass)):
            curClass = allClass[i]
            Parameters = autogen[curClass]['Parameters']
            stringKeys = autogen[curClass]['StringParam'].keys()
            stringParam = autogen[curClass]['StringParam']
            HasGetCustomParam = autogen[curClass]['HasGetCustomParam']
            HasGet = autogen[curClass]['HasGet']
            mapName = "ParamsMap" + curClass
            if HasGet:
                if(len(Parameters) == 0 and not HasGetCustomParam):
                    print tab * " ", getFunction.format(curClass)
                    print tab * " ", "{"
                    tab = tab + tabsize
                    print tab * " ", "return " + parentClass[curClass][0] + "::get(param, unitType);"
                    tab = tab - tabsize
                    print tab * " ", "}"
                    continue

                if(HasGetCustomParam):
                    print tab * " ", "double " + curClass + "::custom_get(const string &param, units_t unitType) const"
                    print tab * " ", "{"
                    print tab * " ", "    return kNullVal;"
                    print tab * " ", "}"
                    print tab * " ", "/* Is this a custom parameter? */"
                    print tab * " ", "static bool " + curClass + "CustomGetCheck(const string &param)"
                    print tab * " ", "{"
                    tab = tab + tabsize
                    print tab * " ", "return CustomParamGet" + curClass + ".find(param) != CustomParamGet" + curClass + ".end();"
                    tab = tab - tabsize
                    print tab * " ", "}"

                print tab * " ", getFunction.format(curClass)
                print tab * " ", "{"
                tab = tab + tabsize
                print tab * " ", "double val = kNullVal;"
                #
                # Need to return custom parameter if it is in tthe GetSet
                #
                if(HasGetCustomParam):
                    print tab * " ", "if(" + curClass + "CustomGetCheck(param)) {"
                    tab = tab + tabsize
                    print tab * " ", "return custom_get(param, unitType);"
                    tab = tab - tabsize
                    print tab * " ", "}"

                print tab * " ", "auto it = " + mapName + ".find(param);"
                print

                print tab * " ", "if(it == " + mapName + ".end())"
                print tab * " ", "{"
                print tab * " ", "    return  " + parentClass[curClass][0] + "::get(param, unitType);"
                print tab * " ", "}"
                print tab * " ", "switch (it->second)"
                print tab * " ", "{"
                tab = tab + tabsize
                for (j, param) in enumerate(Parameters.keys()):
                    print tab * " ", "case " + curClass + "Params::" + stringKeys[j].upper() + ":"
                    if(param == "custom"):
                        print tab * " ", "    val = custom_get(param, unitType);"
                    else:
                        print tab * " ", "    val = " + Parameters[param].format(stringParam[param]) + ";"
                    print tab * " ", "    break;"
                print tab * " ", "default:"
                if len(parentClass[curClass]) != 0:
                    print tab * " ", "    val = " + parentClass[curClass][0] + "::get(param, unitType);"
                else:
                    print tab * " ", "/* No parent class to " + curClass + "*/"
                print tab * " ", "    break;"
                tab = tab - tabsize
                print tab * " ", "}"
                print tab * " ", "return val;"
                tab = tab - tabsize
                print tab * " ", "}"
                print

    def printGetPString(self, autogen, allClass, parentClass):
        """
        """

        tab = self.tab
        for i in range(len(allClass)):
            curClass = allClass[i]

            if autogen[curClass]['HasParameterString']:

                HasSetString = autogen[curClass]['HasSetString']
                HasGetString = autogen[curClass]['HasGetString']

                HasSetCustomString = autogen[curClass]['HasSetStringCustomParam']
                HasGetCustomString = autogen[curClass]['HasGetStringCustomParam']

                HasSetParams = autogen[curClass]['HasSet']
                HasGetParams = autogen[curClass]['HasGet']

                HasSetCustomParams = autogen[curClass]['HasSetCustomParam']
                HasGetCustomParams = autogen[curClass]['HasGetCustomParam']

                HasSetFlag = autogen[curClass]['HasSetFlag']
                HasGetFlag = autogen[curClass]['HasGetFlag']

                HasSetCustomFlags = autogen[curClass]['HasSetFlagCustomParam']
                HasGetCustomFlags = autogen[curClass]['HasGetFlagCustomParam']

                mapName = "ParamsMap" + curClass
                flagName = "FlagsMap" + curClass
                getName = "CustomParamGet" + curClass
                flagGetName = "CustomFlagGet" + curClass
                stringGetName = "CustomParamGetString" + curClass
                setName = "CustomParamSet" + curClass
                flagSetName = "CustomFlagSet" + curClass
                stringSetName = "CustomParamSetString" + curClass

                print tab * " ", "void " + curClass + "::getParameterStrings (stringVec &pstr, paramStringType pstype) const"
                print tab * " ", "{"
                tab = tab + tabsize
                if parentClass[curClass] == []:
                    parentClass[curClass].append("coreObject")

                print tab * " ", "getParamString <" + curClass + ", " + parentClass[curClass][0] + \
                            "> (this, pstr, allowedNumericalParameters" + curClass + ", allowedStringParameters" + \
                            curClass + ", allowedFlags" + curClass + ", pstype);"
                tab = tab - tabsize
                print tab * " ", "}"


def main():
    # Initialized some global variables.
    index = clang.cindex.Index.create()
    # myPath = os.path.dirname(sys.argv[1])
    myFilename = os.path.basename(sys.argv[1])
    includes = "-I/software/griddyn/src/griddyn -I/software/griddyn/src/" + \
        "-I/software/griddyn/src/utilities -I/software/griddyn/gridDyn"
    includes = includes.split()
    myFileParse = Parse()
    # dump_children(index.parse(sys.argv[1], args=includes + ["-std=c++14"]).cursor, myFilename)
    # node = index.parse(sys.argv[1], args=includes + ["-std=c++14"],
    #                   options = clang.cindex.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD).cursor
    node = index.parse(sys.argv[1], args=includes + ["-std=c++14"]).cursor

    namespaceList, autogen, allClass, parentClass = myFileParse.dump_children(
        node, myFilename)
    if autogen["HasMacro"]:
        myPrint = createFile()
        myPrint.printHeader(namespaceList, autogen, allClass)
        myPrint.printGetFunction(autogen, allClass, parentClass)
        myPrint.printSetFunction(autogen, allClass, parentClass)
        myPrint.printSetFlag(autogen, allClass, parentClass)
        myPrint.printGetFlag(autogen, allClass, parentClass)
        myPrint.printSetString(autogen, allClass, parentClass)
        myPrint.printGetString(autogen, allClass, parentClass)
        myPrint.printGetPString(autogen, allClass, parentClass)
        myPrint.printFooter(namespaceList)


if __name__ == "__main__":
    sys.exit(main())
