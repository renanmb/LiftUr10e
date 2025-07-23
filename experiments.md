# Experiments

Log of experiments

the original was trained with 400 envs

```python
python scripts/rsl_rl/train.py --task Template-Liftur10e-v0 --num_envs 400
```
Suggested changes

2 Reward Function and Task Design

For the reward function and reset logic, I am currently using the Franka robot setup as a baseline, as detailed

https://github.com/isaac-sim/IsaacLab/blob/main/source/isaaclab_tasks/isaaclab_tasks/manager_based/manipulation/lift/lift_env_cfg.py

3 rsl_rl and Training Hyperparameters

Using the updated setup, I launched a new training experiment with the rsl_rl library, running 400 parallel environments. The following hyperparameters were manually tuned:

- max_iterations = 2000
- num_steps_per_env = 32
- actor_hidden_dims = [512, 256, 128]
- critic_hidden_dims = [512, 256, 128]
- entropy_coeff = 0.01
- learning_rate = 3e-4
- num_mini_batches = 8
- gamma = 0.99



## Experiment 1

it froze at the ending ```Learning iteration 1999/2000 ```

the hyperparameters used:

```python
from isaaclab.utils import configclass

from isaaclab_rl.rsl_rl import RslRlOnPolicyRunnerCfg, RslRlPpoActorCriticCfg, RslRlPpoAlgorithmCfg


@configclass
class PPORunnerCfg(RslRlOnPolicyRunnerCfg):
    num_steps_per_env = 32
    max_iterations = 2000
    save_interval = 50
    experiment_name = "ur10e_lift"
    empirical_normalization = False
    policy = RslRlPpoActorCriticCfg(
        init_noise_std=1.0,
        actor_hidden_dims=[512, 256, 128],
        critic_hidden_dims=[512, 256, 128],
        activation="elu",
    )
    algorithm = RslRlPpoAlgorithmCfg(
        value_loss_coef=1.0,
        use_clipped_value_loss=True,
        clip_param=0.2,
        entropy_coef=0.01,
        num_learning_epochs=5,
        num_mini_batches=8,
        learning_rate=3.0e-4,
        schedule="adaptive",
        gamma=0.99,
        lam=0.95,
        desired_kl=0.01,
        max_grad_norm=1.0,
    )
```


```bash
Learning iteration 1999/2000                      

                       Computation: 45249 steps/s (collection: 2.739s, learning 0.157s)
             Mean action noise std: 8.58
          Mean value_function loss: 5.2073
               Mean surrogate loss: 0.0018
                 Mean entropy loss: 24.8264
                       Mean reward: 108.91
               Mean episode length: 500.00
    Episode_Reward/reaching_object: 1.4292
     Episode_Reward/lifting_object: 8.8768
Episode_Reward/object_goal_tracking: 1.2053
Episode_Reward/object_goal_tracking_fine_grained: 0.0000
        Episode_Reward/action_rate: -0.2446
          Episode_Reward/joint_vel: -0.0235
Metrics/object_pose/position_error: 0.4207
Metrics/object_pose/orientation_error: 2.0971
      Episode_Termination/time_out: 9.4062
Episode_Termination/object_dropping: 0.0312
--------------------------------------------------------------------------------
                   Total timesteps: 262144000
                    Iteration time: 2.90s
                      Time elapsed: 01:56:15
                               ETA: 00:00:03
```                               

## experiment 2

Now training with only 400 envs and 2000 iterations it trains faster and has better results but the gripper is not closing.

```python
from isaaclab.utils import configclass

from isaaclab_rl.rsl_rl import RslRlOnPolicyRunnerCfg, RslRlPpoActorCriticCfg, RslRlPpoAlgorithmCfg


@configclass
class PPORunnerCfg(RslRlOnPolicyRunnerCfg):
    num_steps_per_env = 32
    max_iterations = 2000
    save_interval = 50
    experiment_name = "ur10e_lift"
    empirical_normalization = False
    policy = RslRlPpoActorCriticCfg(
        init_noise_std=1.0,
        actor_hidden_dims=[512, 256, 128],
        critic_hidden_dims=[512, 256, 128],
        activation="elu",
    )
    algorithm = RslRlPpoAlgorithmCfg(
        value_loss_coef=1.0,
        use_clipped_value_loss=True,
        clip_param=0.2,
        entropy_coef=0.01,
        num_learning_epochs=5,
        num_mini_batches=8,
        learning_rate=3.0e-4,
        schedule="adaptive",
        gamma=0.99,
        lam=0.95,
        desired_kl=0.01,
        max_grad_norm=1.0,
    )
```

Possible issues

1 - USD File and Mimic Joints:

In my USD file, only one joint — the right outer knuckle joint — is currently defined as a mimic joint. Could this indicate an incomplete configuration of the Robotiq 2F-140 gripper?

In the ArticulationCfg, I’ve only defined "finger_joint" as the actuator for the gripper. Is that sufficient to control the gripper effectively, or should other joints be explicitly included in the actuator list as well?


2 - Gain Tuner and Joint Parameters:

I was only able to modify the Natural Frequency and Damping Ratio for the mimic joint. Could this suggest a misconfiguration in the USD file for the other joints?

3 - Reward Function and Reset Logic:

I’m currently using the reward and reset structure from the Franka Lift environment as a baseline. Is this a reasonable baseline for my UR10e + 2F-140 setup, or would you recommend adapting it further to better suit this task?

4 - Training Stability and Policy Robustness:

As seen in the training plots and video, the robot can now grasp the cube, but it still struggles to consistently complete a stable lift. Do you have any practical suggestions to improve training stability, enhance policy generalization, and ensure the robot can reliably complete the task?
