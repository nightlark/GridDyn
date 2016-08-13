/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil;  eval: (c-set-offset 'innamespace 0); -*- */
/*
* LLNS Copyright Start
* Copyright (c) 2016, Lawrence Livermore National Security
* This work was performed under the auspices of the U.S. Department
* of Energy by Lawrence Livermore National Laboratory in part under
* Contract W-7405-Eng-48 and in part under Contract DE-AC52-07NA27344.
* Produced at the Lawrence Livermore National Laboratory.
* All rights reserved.
* For details, see the LICENSE file.
* LLNS Copyright End
*/

#include "exeTestHelper.h"
#include <boost/filesystem.hpp>
#include <cstdlib>
#include <fstream>
#include <streambuf>

int exeTestRunner::counter = 1;

exeTestRunner::exeTestRunner()
{
	++counter;
	outFile = "exeText_" + std::to_string(counter) + ".out";
}

exeTestRunner::exeTestRunner(const std::string &baseLocation, const std::string &target)
{
	++counter;
	outFile = "exeText_" + std::to_string(counter) + ".out";
	active=findFileLocation(baseLocation, target);
}

bool exeTestRunner::findFileLocation(const std::string &baseLocation, const std::string &target)
{
	boost::filesystem::path sourcePath(baseLocation);

	auto tryPath1 = sourcePath / target;
	if (boost::filesystem::exists(tryPath1))
	{
		exeString = tryPath1.string();
		return true;
	}

	auto tryPath2 = sourcePath / (target + ".exe");
	if (boost::filesystem::exists(tryPath2))
	{
		exeString = tryPath2.string();
		return true;
	}
	#ifndef NDEBUG
	auto tryPathD1 = sourcePath /"Debug"/ target;
	if (boost::filesystem::exists(tryPathD1))
	{
		exeString = tryPathD1.string();
		return true;
	}

	auto tryPathD2 = sourcePath / "Debug" / (target + ".exe");
	if (boost::filesystem::exists(tryPathD2))
	{
		exeString = tryPathD2.string();
		return true;
	}
	#endif
	auto tryPathR1 = sourcePath / "Release" / target;
	if (boost::filesystem::exists(tryPathR1))
	{
		exeString = tryPathR1.string();
		return true;
	}

	auto tryPathR2 = sourcePath / "Release" / (target + ".exe");
	if (boost::filesystem::exists(tryPathR2))
	{
		exeString = tryPathR2.string();
		return true;
	}

	return false;
}

int exeTestRunner::run(const std::string &args) const
{
	if (!active)
	{
		return -101;
	}
	std::string rstr = exeString + " " + args;
	return system(rstr.c_str());
}

std::string exeTestRunner::runCaptureOutput(const std::string &args) const
{
	if (!active)
	{
		return "invalid executable";
	}
	std::string rstr = exeString + " " + args+" > "+outFile;
	system(rstr.c_str());


	std::ifstream t(outFile);
	std::string str((std::istreambuf_iterator<char>(t)),
		std::istreambuf_iterator<char>());

	remove(outFile.c_str());
	return str;

}