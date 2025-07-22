# Error logging to fix

Trying to keep tracks of issues

## Error 1

https://github.com/isaac-sim/IsaacLab/issues/1539

This error ```malloc(): invalid size (unsorted)``` not very descriptive

It seems to be related to the 4096 environments exceeding the system memory

```bash
2025-07-22 18:37:19 [0ms] [Warning] [omni.kit.app.plugin] No crash reporter present, dumps uploading isn't available.
2025-07-22 18:37:19 [1ms] [Warning] [omni.ext.plugin] [ext: rendering_modes] Extensions config 'extension.toml' doesn't exist '/home/goat/Documents/GitHub/renanmb/IsaacLab/apps/rendering_modes' or '/home/goat/Documents/GitHub/renanmb/IsaacLab/apps/rendering_modes/config'
2025-07-22 18:37:19 [231ms] [Warning] [omni.datastore] OmniHub is inaccessible
|---------------------------------------------------------------------------------------------|
| Driver Version: 570.169       | Graphics API: Vulkan
|=============================================================================================|
| GPU | Name                             | Active | LDA | GPU Memory | Vendor-ID | LUID       |
|     |                                  |        |     |            | Device-ID | UUID       |
|     |                                  |        |     |            | Bus-ID    |            |
|---------------------------------------------------------------------------------------------|
| 0   | NVIDIA GeForce RTX 3090          | Yes: 0 |     | 24576   MB | 10de      | 0          |
|     |                                  |        |     |            | 2204      | 4f951f2e.. |
|     |                                  |        |     |            | 1         |            |
|=============================================================================================|
| OS: 22.04.5 LTS (Jammy Jellyfish) ubuntu, Version: 22.04.5, Kernel: 6.8.0-64-generic
| XServer Vendor: The X.Org Foundation, XServer Version: 12101004 (1.21.1.4)
| Processor: AMD Ryzen 9 9950X 16-Core Processor
| Cores: 16 | Logical Cores: 32
|---------------------------------------------------------------------------------------------|
| Total Memory (MB): 96100 | Free Memory: 86487
| Total Page/Swap (MB): 2047 | Free Page/Swap: 2047
|---------------------------------------------------------------------------------------------|
2025-07-22 18:37:20 [866ms] [Warning] [gpu.foundation.plugin] IOMMU is enabled.
2025-07-22 18:37:22 [2,768ms] [Warning] [omni.log] Source: omni.hydra was already registered.
2025-07-22 18:37:22 [2,991ms] [Warning] [omni.isaac.dynamic_control] omni.isaac.dynamic_control is deprecated as of Isaac Sim 4.5. No action is needed from end-users.
2025-07-22 18:37:23 [3,834ms] [Warning] [omni.replicator.core.scripts.extension] No material configuration file, adding configuration to material settings directly.
2025-07-22 18:37:24 [4,273ms] [Warning] [omni.kit.menu.utils.app_menu] add_menu_items: menu [<MenuItemDescription name:'New'>, <MenuItemDescription name:'Open'>, <MenuItemDescription name:'Re-open with New Edit Layer'>, <MenuItemDescription name:'Save'>, <MenuItemDescription name:'Save With Options'>, <MenuItemDescription name:'Save As...'>, <MenuItemDescription name:'Save Flattened As...'>, <MenuItemDescription name:'Add Reference'>, <MenuItemDescription name:'Add Payload'>, <MenuItemDescription name:'Exit'>] cannot change delegate
2025-07-22 18:37:25 [5,394ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 7508933632
2025-07-22 18:37:25 [5,394ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid false, within: false
2025-07-22 18:37:25 [5,394ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : decrement: 167690, decrement size: 7433845248
2025-07-22 18:37:25 [5,394ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : New limit 9574251 (slope: 447, intercept: 13179904)
2025-07-22 18:37:25 [5,394ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 4287216384
2025-07-22 18:37:25 [5,394ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid true, within: true
2025-07-22 18:37:25 [5,472ms] [Warning] [omni.usd-abi.plugin] No setting was found for '/rtx-defaults-transient/meshlights/forceDisable'
[7.056s] Simulation App Startup Complete
[INFO]: Parsing configuration from: LiftUr10e.tasks.manager_based.liftur10e.liftur10e_env_cfg:Liftur10eEnvCfg
2025-07-22 18:37:26 [7,066ms] [Warning] [isaaclab.envs.manager_based_env] Seed not set for the environment. The environment creation may not be deterministic.
[7.098s] [ext: omni.physx.fabric-106.5.7] startup
[INFO]: Base environment:
        Environment device    : cuda:0
        Environment seed      : None
        Physics step-size     : 0.01
        Rendering step-size   : 0.02
        Environment step-size : 0.02
[INFO]: Time taken for scene creation : 6.915844 seconds
[INFO]: Scene manager:  <class InteractiveScene>
        Number of environments: 4096
        Environment spacing   : 4.0
        Source prim name      : /World/envs/env_0
        Global prim paths     : []
        Replicate physics     : True
[INFO]: Starting the simulation. This may take a few seconds. Please wait...
malloc(): invalid size (unsorted)
Aborted (core dumped)
```

## error 2

Something is wrong on the setup, it starts to throw these errors at ```Learning iteration 5/2000```

Patch buffer overflow detected, please increase its size to at least 266360

```bash
2025-07-22 19:14:29 [46,804ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 266360 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
```

[[Question] Is there a solution for the Patch buffer overflow error? #931](https://github.com/isaac-sim/IsaacLab/issues/931)


```bash
################################################################################
                       Learning iteration 10/2000                       

                       Computation: 36373 steps/s (collection: 3.450s, learning 0.154s)
             Mean action noise std: 1.05
          Mean value_function loss: 0.0307
               Mean surrogate loss: 0.0003
                 Mean entropy loss: 10.2677
                       Mean reward: 0.67
               Mean episode length: 340.15
    Episode_Reward/reaching_object: 0.0547
     Episode_Reward/lifting_object: 0.0685
Episode_Reward/object_goal_tracking: 0.0091
Episode_Reward/object_goal_tracking_fine_grained: 0.0000
        Episode_Reward/action_rate: -0.0010
          Episode_Reward/joint_vel: -0.0751
Metrics/object_pose/position_error: 0.3329
Metrics/object_pose/orientation_error: 2.8862
      Episode_Termination/time_out: 8.4688
Episode_Termination/object_dropping: 0.1562
--------------------------------------------------------------------------------
                   Total timesteps: 1441792
                    Iteration time: 3.60s
                      Time elapsed: 00:00:35
                               ETA: 01:46:48

2025-07-22 19:14:29 [46,804ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 266360 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:29 [46,852ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 266288 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:29 [46,905ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 265163 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:29 [46,952ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 265559 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:29 [47,004ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 265298 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:29 [47,052ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 264973 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:29 [47,105ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 264863 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:29 [47,153ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 264756 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:29 [47,205ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 264526 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:29 [47,257ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 265158 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:29 [47,318ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 263866 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,367ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 264328 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,421ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 263740 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,470ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 264447 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,525ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 263647 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,574ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 264108 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,628ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 264101 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,677ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 265075 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,729ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 265536 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,777ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 266171 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,829ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 266078 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,877ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 267167 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,930ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 267434 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [47,978ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 267145 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [48,031ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 266465 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [48,078ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 267345 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [48,130ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 268127 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [48,179ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 268878 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [48,232ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 269373 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [48,280ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 271242 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:30 [48,334ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 269983 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,383ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 270322 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,436ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 270602 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,484ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 271885 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,538ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 272379 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,586ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 273023 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,640ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 273331 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,689ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 274229 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,743ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 274852 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,793ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 275472 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,848ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 275153 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,896ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 275811 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,949ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 275561 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [48,998ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 276723 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [49,050ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 276677 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [49,098ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 277203 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [49,149ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 276880 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [49,196ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 277856 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [49,248ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 277643 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [49,298ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 278118 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:31 [49,350ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 278207 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:32 [49,400ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 279603 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:32 [49,452ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 279500 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:32 [49,500ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 280329 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
2025-07-22 19:14:32 [49,552ms] [Error] [omni.physx.plugin] PhysX error: Patch buffer overflow detected, please increase its size to at least 280442 in the scene desc!
, FILE /builds/omniverse/physics/physx/source/gpunarrowphase/src/PxgNarrowphaseCore.cpp, LINE 1599
```