/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 3.0.12
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package com.java.griddyn;

public class griddynJNI {
  static {
    System.loadLibrary("JNIgriddynd");
  }
  public final static native long new_doublep();
  public final static native long copy_doublep(double jarg1);
  public final static native void delete_doublep(long jarg1);
  public final static native void doublep_assign(long jarg1, double jarg2);
  public final static native double doublep_value(long jarg1);
  public final static native String new_charp();
  public final static native String copy_charp(char jarg1);
  public final static native void delete_charp(String jarg1);
  public final static native void charp_assign(String jarg1, char jarg2);
  public final static native char charp_value(String jarg1);
  public final static native long new_doubleArray(int jarg1);
  public final static native void delete_doubleArray(long jarg1);
  public final static native double doubleArray_getitem(long jarg1, doubleArray jarg1_, int jarg2);
  public final static native void doubleArray_setitem(long jarg1, doubleArray jarg1_, int jarg2, double jarg3);
  public final static native long doubleArray_cast(long jarg1, doubleArray jarg1_);
  public final static native long doubleArray_frompointer(long jarg1);
  public final static native int gridDynSimulation_getResults__SWIG_0(long jarg1, String jarg2, long jarg3, int jarg4);
  public final static native int griddyn_ok_get();
  public final static native int griddyn_invalid_object_get();
  public final static native int griddyn_invalid_parameter_value_get();
  public final static native int griddyn_unknown_parameter_get();
  public final static native int griddyn_add_failure_get();
  public final static native int griddyn_remove_failure_get();
  public final static native int griddyn_query_load_failure_get();
  public final static native int griddyn_file_load_failure_get();
  public final static native int griddyn_solve_error_get();
  public final static native int griddyn_object_not_initialized_get();
  public final static native int griddyn_invalid_function_call_get();
  public final static native int griddyn_function_failure_get();
  public final static native int GRIDDYN_PENDING_get();
  public final static native int GRIDDYN_COMPLETE_get();
  public final static native long gridDynObject_create(String jarg1, String jarg2);
  public final static native long gridDynObject_clone(long jarg1);
  public final static native void gridDynObject_free(long jarg1);
  public final static native int gridDynObject_add(long jarg1, long jarg2);
  public final static native int gridDynObject_remove(long jarg1, long jarg2);
  public final static native int gridDynObject_setString(long jarg1, String jarg2, String jarg3);
  public final static native int gridDynObject_setValue(long jarg1, String jarg2, double jarg3);
  public final static native int gridDynObject_setValueUnits(long jarg1, String jarg2, double jarg3, String jarg4);
  public final static native int gridDynObject_setFlag(long jarg1, String jarg2, int jarg3);
  public final static native int gridDynObject_getString(long jarg1, String jarg2, String jarg3, int jarg4);
  public final static native int gridDynObject_getValue(long jarg1, String jarg2, long jarg3);
  public final static native int gridDynObject_getValueUnits(long jarg1, String jarg2, String jarg3, long jarg4);
  public final static native int gridDynObject_getFlag(long jarg1, String jarg2, long jarg3);
  public final static native long gridDynObject_find(long jarg1, String jarg2);
  public final static native long gridDynObject_getSubObject(long jarg1, String jarg2, int jarg3);
  public final static native long gridDynObject_findByUserId(long jarg1, String jarg2, int jarg3);
  public final static native long gridDynObject_getParent(long jarg1);
  public final static native String gridDynObject_getType(long jarg1);
  public final static native long gridDynSimulation_create(String jarg1, String jarg2);
  public final static native void gridDynSimulation_free(long jarg1);
  public final static native int gridDynSimulation_initializeFromString(long jarg1, String jarg2);
  public final static native int gridDynSimulation_initializeFromArgs(long jarg1, int jarg2, long jarg3, int jarg4);
  public final static native int gridDynSimulation_loadfile(long jarg1, String jarg2, String jarg3);
  public final static native int gridDynSimulation_addCommand(long jarg1, String jarg2);
  public final static native int gridDynSimulation_powerflowInitialize(long jarg1);
  public final static native int gridDynSimulation_powerflow(long jarg1);
  public final static native int gridDynSimulation_dynamicInitialize(long jarg1);
  public final static native int gridDynSimulation_reset(long jarg1);
  public final static native double gridDynSimulation_getCurrentTime(long jarg1);
  public final static native int gridDynSimulation_run(long jarg1);
  public final static native int gridDynSimulation_runTo(long jarg1, double jarg2);
  public final static native int gridDynSimulation_Step(long jarg1);
  public final static native int gridDynSimulation_runAsync(long jarg1);
  public final static native int gridDynSimulation_runToAsync(long jarg1, double jarg2);
  public final static native int gridDynSimulation_StepAsync(long jarg1);
  public final static native int gridDynSimulation_getStatus(long jarg1);
  public final static native long getSimulationObject(long jarg1);
  public final static native long gridDynSimulation_getSolverKey(long jarg1, String jarg2);
  public final static native void gridDynSolverKey_free(long jarg1);
  public final static native int gridDynSimulation_stateSize(long jarg1, long jarg2);
  public final static native int gridDynSimulation_busCount(long jarg1);
  public final static native int gridDynSimulation_lineCount(long jarg1);
  public final static native int gridDynSimulation_guessState(long jarg1, double jarg2, long jarg3, long jarg4, long jarg5);
  public final static native int gridDynSimulation_setState(long jarg1, double jarg2, long jarg3, long jarg4, long jarg5);
  public final static native int gridDynSimulation_getStateVariableTypes(long jarg1, long jarg2, long jarg3);
  public final static native int gridDynSimulation_residual(long jarg1, double jarg2, long jarg3, long jarg4, long jarg5, long jarg6);
  public final static native int gridDynSimulation_derivative(long jarg1, double jarg2, long jarg3, long jarg4, long jarg5);
  public final static native int gridDynSimulation_algebraicUpdate(long jarg1, double jarg2, long jarg3, long jarg4, double jarg5, long jarg6);
  public final static native int gridDynSimulation_jacobian(long jarg1, double jarg2, long jarg3, long jarg4, double jarg5, long jarg6, long jarg7);
  public final static native long gridDynSingleQuery_create(long jarg1, String jarg2);
  public final static native long gridDynVectorQuery_create(long jarg1, String jarg2);
  public final static native void gridDynSingleQuery_free(long jarg1);
  public final static native void gridDynVectorQuery_free(long jarg1);
  public final static native double gridDynSingleQuery_run(long jarg1);
  public final static native int gridDynVectorQuery_run(long jarg1, long jarg2, int jarg3);
  public final static native int gridDynVectorQuery_append(long jarg1, long jarg2, String jarg3);
  public final static native int gridDynSingleQuery_update(long jarg1, long jarg2, String jarg3);
  public final static native int gridDynVectorQuery_update(long jarg1, long jarg2, String jarg3);
  public final static native long gridDynEvent_create(String jarg1, long jarg2);
  public final static native void gridDynEvent_free(long jarg1);
  public final static native int gridDynEvent_trigger(long jarg1);
  public final static native int gridDynEvent_schedule(long jarg1, long jarg2);
  public final static native int gridDynEvent_setValue(long jarg1, String jarg2, double jarg3);
  public final static native int gridDynEvent_setString(long jarg1, String jarg2, String jarg3);
  public final static native int gridDynEvent_setFlag(long jarg1, String jarg2, int jarg3);
  public final static native int gridDynEvent_setTarget(long jarg1, long jarg2);
  public final static native int gridDynObject_stateSize(long jarg1, long jarg2);
  public final static native int gridDynObject_guessState(long jarg1, double jarg2, long jarg3, long jarg4, long jarg5);
  public final static native int gridDynObject_setState(long jarg1, double jarg2, long jarg3, long jarg4, long jarg5);
  public final static native int gridDynObject_getStateVariableTypes(long jarg1, long jarg2, long jarg3);
  public final static native int gridDynObject_residual(long jarg1, long jarg2, int jarg3, long jarg4, long jarg5);
  public final static native int gridDynObject_derivative(long jarg1, long jarg2, int jarg3, long jarg4, long jarg5);
  public final static native int gridDynObject_algebraicUpdate(long jarg1, long jarg2, int jarg3, long jarg4, double jarg5, long jarg6);
  public final static native int gridDynObject_jacobian(long jarg1, long jarg2, int jarg3, double jarg4, long jarg5, long jarg6);
  public final static native int gridDynObject_ioPartialDerivatives(long jarg1, long jarg2, int jarg3, long jarg4, long jarg5);
  public final static native int gridDynObject_outputPartialDerivatives(long jarg1, long jarg2, int jarg3, long jarg4, long jarg5);
}
