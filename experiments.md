# Experiments

Log of experiments

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