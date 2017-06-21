# LLNS Copyright Start
# Copyright (c) 2017, Lawrence Livermore National Security
# This work was performed under the auspices of the U.S. Department 
# of Energy by Lawrence Livermore National Laboratory in part under 
# Contract W-7405-Eng-48 and in part under Contract DE-AC52-07NA27344.
# Produced at the Lawrence Livermore National Laboratory.
# All rights reserved.
# For details, see the LICENSE file.
# LLNS Copyright End

#project  GriddDyn

set(genmodel_headers
    GenModel.h
	genmodels/GenModelClassical.h
	genmodels/GenModel3.h
	genmodels/GenModel4.h
	genmodels/GenModel5.h
	genmodels/GenModel5type2.h
	genmodels/GenModel5type3.h
	genmodels/GenModel6.h	
	genmodels/GenModel6type2.h	
	genmodels/GenModelGENROU.h	
	genmodels/GenModel8.h
	genmodels/GenModelInverter.h
	genmodels/otherGenModels.h
	)
	
set(genmodel_sources
	${genmodel_headers}
	genmodels/GenModel.cpp
	genmodels/GenModelClassical.cpp
	genmodels/GenModel3.cpp
	genmodels/GenModel4.cpp
	genmodels/GenModel5.cpp
	genmodels/GenModel5type2.cpp
	genmodels/GenModel5type3.cpp
	genmodels/GenModel6.cpp	
	genmodels/GenModel6type2.cpp	
	genmodels/GenModelGENROU.cpp	
	genmodels/GenModel8.cpp
	genmodels/GenModelInverter.cpp
	)

set(generator_headers
	Generator.h
	generators/variableGenerator.h
	generators/isocController.h
	generators/DynamicGenerator.h
	)
	
set (generator_sources
	${generator_headers}
	generators/Generator.cpp
	generators/variableGenerator.cpp
	generators/isocController.cpp
	generators/DynamicGenerator.cpp
	)

set(gridSource_sources
	Source.h
	sources/sourceTypes.h
	sources/rampSource.h
	sources/fileSource.h
	sources/randomSource.h
	sources/pulseSource.h
	sources/sineSource.h
	sources/functionSource.h
	sources/commSource.h
	sources/blockSource.h
	sources/grabberSource.h
	sources/Source.cpp
	sources/rampSource.cpp
	sources/fileSource.cpp
	sources/randomSource.cpp
	sources/pulseSource.cpp
	sources/sineSource.cpp
	sources/functionSource.cpp
	sources/commSource.cpp
	sources/blockSource.cpp
	sources/grabberSource.cpp
	)

set(exciter_sources
	exciters/ExciterDC1A.h
	exciters/ExciterDC2A.h
	exciters/ExciterIEEEtype1.h
	exciters/ExciterIEEEtype2.h
	exciters/Exciter.cpp
	exciters/ExciterDC1A.cpp
	exciters/ExciterDC2A.cpp
	exciters/ExciterIEEEtype1.cpp
	exciters/ExciterIEEEtype2.cpp
	stabilizers/Stabilizer.cpp
	Exciter.h
	Stabilizer.h
	)
	

	
set(gov_sources

	governors/GovernorHydro.h
	governors/GovernorIeeeSimple.h
	governors/GovernorReheat.h
	governors/GovernorSteamNR.h
	governors/GovernorSteamTCSR.h
	governors/GovernorTgov1.h
	governors/Governor.cpp
	governors/GovernorHydro.cpp
	governors/GovernorIeeeSimple.cpp
	governors/GovernorReheat.cpp
	governors/GovernorSteamNR.cpp
	governors/GovernorSteamTCSR.cpp
	governors/GovernorTgov1.cpp
	Governor.h
	governors/GovernorTypes.h
	)

set (block_sources
	blocks/Block.cpp
	blocks/integralBlock.cpp
	blocks/integralBlock.h
	blocks/deadbandBlock.cpp
	blocks/deadbandBlock.h
	blocks/delayBlock.cpp
	blocks/delayBlock.h
	blocks/nullBlock.h
	blocks/nullBlock.cpp
	blocks/pidBlock.cpp
	blocks/pidBlock.h
	blocks/controlBlock.cpp
	blocks/controlBlock.h
	blocks/derivativeBlock.cpp
	blocks/derivativeBlock.h
	blocks/functionBlock.cpp
	blocks/functionBlock.h
	blocks/lutBlock.cpp
	blocks/lutBlock.h
	blocks/transferFunctionBlock.cpp
	blocks/transferFunctionBlock.h
	blocks/filteredDerivativeBlock.cpp
	blocks/filteredDerivativeBlock.h
	blocks/blockSequence.cpp
	blocks/blockSequence.h
	blocks/valueLimiter.cpp
	blocks/valueLimiter.h
	blocks/rampLimiter.cpp
	blocks/rampLimiter.h
	blocks/blockLibrary.h
	Block.h
	)
	
set(submodel_sources
	${genmodel_sources}
	${exciter_sources}
	${gov_sources}
	${gridSource_sources}
	${block_sources}
	)

set(submodel_headers
	Exciter.h
	Stabilizer.h
	Source.h
	GenModel.h
	otherGenModels.h
	Governor.h
	gridControlBlocks.h
	)
	
set(load_headers

	Load.h
	loads/otherLoads.h
	loads/rampLoad.h
	loads/exponentialLoad.h
	loads/sourceLoad.h
	loads/fileLoad.h
	loads/fDepLoad.h
	loads/motorLoad.h
	loads/gridLabDLoad.h
	loads/svd.h
	loads/aggregateLoad.h
	loads/zipLoad.h
	loads/ThreePhaseLoad.h
	)
	
set(load_sources
	${load_headers}
	loads/Load.cpp
	loads/rampLoad.cpp
	loads/fileLoad.cpp
	loads/motorLoad.cpp
	loads/motorLoad3.cpp
	loads/motorLoad5.cpp
	loads/gridLabDLoad.cpp
	loads/exponentialLoad.cpp
	loads/fDepLoad.cpp
	loads/aggregateLoad.cpp
	loads/sourceLoad.cpp
	loads/zipLoad.cpp
	loads/svd.cpp
	loads/ThreePhaseLoad.cpp
	)

set (link_headers
	links/dcLink.h
	links/acdcConverter.h
	links/adjustableTransformer.h
	Link.h
	links/subsystem.h
	links/hvdc.h
	links/zBreaker.h
	links/longLine.h
	links/acLine.h
	)
	
set(link_sources
	${link_headers}
	links/Link.cpp
	links/adjustableTransformer.cpp
	links/dcLink.cpp
	links/acdcConverter.cpp
	links/subsystem.cpp
	links/hvdc.cpp
	links/zBreaker.cpp
	links/longLine.cpp
	links/acLine.cpp
	)

set(simulation_headers
	simulation/contingency.h
	simulation/continuation.h
	griddyn.h
	simulation/gridSimulation.h
	simulation/diagnostics.h
	simulation/powerFlowErrorRecovery.h
	simulation/dynamicInitialConditionRecovery.h
	simulation/faultResetRecovery.h
	simulation/gridDynActions.h
	simulation/gridDynSimulationFileOps.h
	)
	
set(simulation_sources
	${simulation_headers}
    simulation/gridDynContinuation.cpp
	simulation/gridDynSimulation.cpp	
	simulation/contingency.cpp
	simulation/gridDynPowerFlow.cpp
	simulation/gridDynDynamic.cpp
	simulation/gridSimulation.cpp
	simulation/gridDynActions.cpp
	simulation/gridDynSimulationFileOps.cpp
	simulation/diagnostics.cpp
	simulation/powerFlowErrorRecovery.cpp
	simulation/dynamicInitialConditionRecovery.cpp
	simulation/faultResetRecovery.cpp
	simulation/gridDynContingency.cpp
	
	)

set(solver_headers
	solvers/solverInterface.h
	solvers/sundialsInterface.h
	solvers/idaInterface.h
	solvers/kinsolInterface.h
	solvers/basicSolver.h
	solvers/sundialsMatrixData.h
	solvers/basicOdeSolver.h
	solvers/solverMode.hpp
	)
	
set(solver_sources
	${solver_headers}
	solvers/idaInterface.cpp
	solvers/kinsolInterface.cpp
	solvers/solverInterface.cpp
	solvers/basicSolver.cpp
	solvers/sundialsMatrixDataDense.cpp
	solvers/sundialsMatrixDataSparseRow.cpp
	solvers/sundialsMatrixDataSparseColumn.cpp
	solvers/sundialsInterface.cpp
	solvers/basicOdeSolver.cpp
	)
	
IF (LOAD_CVODE)
	list(APPEND solver_sources 
	solvers/cvodeInterface.cpp
	solvers/cvodeInterface.h
	)

	list(APPEND solver_headers
	solvers/cvodeInterface.h
	)
	
ENDIF(LOAD_CVODE)

IF (LOAD_ARKODE)
	list(APPEND solver_sources 
	solvers/arkodeInterface.cpp
	solvers/arkodeInterface.h
	)

	list(APPEND solver_headers
	solvers/arkodeInterface.h
	)
ENDIF(LOAD_ARKODE)

set (core_headers
	gridComponent.h
	gridPrimary.h
	gridSecondary.h
	gridSubModel.h
	gridObjectsHelperClasses.h
	numericEstimationFunctions.h
	gridDynDefinitions.hpp
	)

set (core_sources
	${core_headers}
	gridComponent.cpp
	gridPrimary.cpp
	gridSecondary.cpp
	gridSubModel.cpp
	gridObjectsHelperClasses.cpp
	numericEstimationFunctions.cpp
	)

set(primary_headers
	gridBus.h
	Area.h
	primary/dcBus.h
	allGridDynObjects.h
	primary/BusControls.h
	primary/listMaintainer.h
	primary/infiniteBus.h
	primary/acBus.h
	primary/DcBusControls.h
	)
	
set(primary_sources
	${primary_headers}
	primary/gridBus.cpp
	primary/Area.cpp		
	primary/dcBus.cpp
	primary/infiniteBus.cpp
	primary/BusControls.cpp
	primary/DcBusControls.cpp
	primary/acBus.cpp
	primary/listMaintainer.cpp
	)

set(event_headers
	events/Event.h
	events/eventAdapters.h
	events/eventQueue.h
	events/eventInterface.hpp
	events/reversibleEvent.h
	events/parameterOperator.h
	events/Player.h
	events/interpolatingPlayer.h
	events/compoundEvent.h
	events/compoundEventPlayer.h
	)
	
set(event_sources
	${event_headers}
	events/Event.cpp
	events/eventAdapters.cpp
	events/eventQueue.cpp
	events/Player.cpp
	events/interpolatingPlayer.cpp
	events/compoundEvent.cpp
	events/compoundEventPlayer.cpp
	events/reversibleEvent.cpp
	events/parameterOperator.cpp
	)	
set(measurement_headers
	measurement/gridGrabbers.h
	measurement/objectGrabbers.h
	measurement/collector.h
	measurement/Recorder.h
	measurement/stateGrabber.h
	measurement/Condition.h
	measurement/grabberSet.h
	measurement/grabberInterpreter.hpp
	)
	
set(measurement_sources
	${measurement_headers}
	measurement/Recorder.cpp
	measurement/gridGrabbers.cpp
	measurement/grabberInterpreter.cpp
	measurement/stateGrabbers.cpp
	measurement/Condition.cpp
	measurement/objectGrabbers.cpp
	measurement/compoundCondition.cpp
	measurement/collector.cpp
	measurement/grabberSet.cpp
	)	

set (comm_headers
	comms/commMessage.h
	comms/Communicator.h
	comms/communicationsCore.h
	comms/relayMessage.h
	comms/schedulerMessage.h
	comms/controlMessage.h
	comms/commManager.h
	)
	
set (comm_sources
	${comm_headers}
	comms/commMessage.cpp
	comms/Communicator.cpp
	comms/communicationsCore.cpp
	comms/relayMessage.cpp
	comms/schedulerMessage.cpp
	comms/controlMessage.cpp
	comms/commManager.cpp
	)
	
set(relay_headers
	Relay.h
	relays/zonalRelay.h
	relays/loadRelay.h
	relays/busRelay.h
	relays/fuse.h
	relays/breaker.h
	relays/sensor.h
	relays/differentialRelay.h
	relays/controlRelay.h
	relays/pmu.h
	)
	
set (relay_sources
	${relay_headers}
	relays/Relay.cpp
	relays/zonalRelay.cpp
	relays/loadRelay.cpp
	relays/busRelay.cpp
	relays/fuse.cpp
	relays/breaker.cpp
	relays/sensor.cpp
	relays/differentialRelay.cpp
	relays/controlRelay.cpp
	relays/pmu.cpp
)


set (controller_headers
	controllers/schedulerInfo.h
	controllers/scheduler.h
	controllers/reserveDispatcher.h
	controllers/AGControl.h
	controllers/controlSystem.h
	controllers/dispatcher.h
	)
	
set (controller_sources
	${controller_headers}
	controllers/scheduler.cpp
	controllers/schedulerRamp.cpp
	controllers/schedulerReg.cpp
	controllers/reserveDispatcher.cpp
	controllers/controlSystem.cpp
	controllers/AGControl.cpp
	controllers/dispatcher.cpp
	)

set(sublibrary_files
	${event_sources}
	${measurement_sources}
	${griddynIO_sources}
	${gridSource_sources}
	${controller_sources}
	${comm_sources}
	${solver_sources}
	)

set(model_files
	${relay_sources}
	${submodel_sources}
	${load_sources}
	${link_sources}
	${generator_sources}
	)


set(header_files
	${core_headers}
	${primary_headers}
	${link_headers}
	${solver_headers}
	${controller_headers}
	${comm_headers}
	${event_headers}
	${measurement_headers}
	${gridDynIO_headers}
	${simulation_headers}
	${submodel_headers}
	${load_headers}
	${relay_headers}
	${generator_headers}
	)


add_library(griddyn STATIC ${simulation_sources} ${model_files} ${core_sources} ${primary_sources} ${sublibrary_files})

source_group("loads" FILES ${load_sources})
source_group("exciters" FILES ${exciter_sources})
source_group("governors" FILES ${gov_sources})
source_group("genmodels" FILES ${genmodel_sources})
source_group("links" FILES ${link_sources})
source_group("events" FILES ${event_sources})
source_group("measurement" FILES ${measurement_sources})
source_group("generators" FILES ${generator_sources})
source_group("sources" FILES ${gridSource_sources})
source_group("simulation" FILES ${simulation_sources})
source_group("core" FILES ${core_sources})
source_group("primary" FILES ${primary_sources})
source_group("relays" FILES ${relay_sources})
source_group("comms" FILES ${comm_sources})
source_group("controllers" FILES ${controller_sources})
source_group("blocks" FILES ${block_sources})
source_group("solvers" FILES ${solver_sources})

INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/src/griddyn)
INCLUDE_DIRECTORIES(SYSTEM ${SUNDIALS_INCLUDE_DIR})

#create a griddyn_config.h file for program options
CONFIGURE_FILE(${PROJECT_SOURCE_DIR}/griddyn-config.h.in ${PROJECT_BINARY_DIR}/libs/include/griddyn-config.h)

INSTALL(TARGETS griddyn
	LIBRARY DESTINATION lib
	ARCHIVE DESTINATION lib)


INSTALL(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  DESTINATION include
  FILES_MATCHING PATTERN "*.h")
