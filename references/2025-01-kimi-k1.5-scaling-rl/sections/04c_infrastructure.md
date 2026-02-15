# 2.6 RL Infrastructure [p. 8-11]

**Figure 3** (p. 8): "Large Scale Reinforcement Learning Training System for LLM"

Description: Two-part diagram showing the RL training system architecture
- **(a) System overview**: Shows the data and weight flow between components: Rollout Workers generate rollout trajectories which are stored in a Replay Buffer. Reward Models (Code, Math, K-12, Vision) evaluate responses via eval requests. A Master coordinates the system. Trainer Workers receive training data from the Replay Buffer and compute gradient updates for the Policy Model and Reference Model. Weight flow goes from Trainer Workers to Rollout Workers; data flow goes from Rollout Workers through the Replay Buffer to Trainer Workers.
- **(b) Partial Rollout**: Shows how the Replay Buffer handles partial rollouts across iterations. From the prompt set, a rollout worker generates responses. Responses can have: normal stop, cut by length (saved for partial rollout), or repeat/early stop. Partial rollouts are saved and continued in subsequent iterations (iteration N).
- Supports claim: The system uses an iterative synchronous RL framework with partial rollouts to enable efficient long-context training

## 2.6.1 Large Scale Reinforcement Learning Training System for LLM [p. 9]

In the realm of artificial intelligence, reinforcement learning (RL) has emerged as a pivotal training methodology for large language models (LLMs) (Ouyang et al. 2022; Jaech et al. 2024), drawing inspiration from its success in mastering complex games like Go, StarCraft II, and Dota 2 through systems such as AlphaGo (Silver et al. 2017), AlphaStar (Vinyals et al. 2019), and OpenAI Dota Five (Berner et al. 2019). Following in this tradition, the Kimi k1.5 system adopts an iterative synchronous RL framework, meticulously designed to bolster the model's reasoning capabilities through persistent learning and adaptation. A key innovation in this system is the introduction of a **Partial Rollout** technique, designed to optimize the handling of complex reasoning trajectories [p. 9].

The RL training system (Figure 3a) operates through an iterative synchronous approach, with each iteration encompassing a **rollout phase** and a **training phase** [p. 9]:
- **Rollout phase**: Rollout workers, coordinated by a central master, generate rollout trajectories by interacting with the model, producing sequences of responses to various inputs. These trajectories are stored in a replay buffer, which ensures a diverse and unbiased dataset for training by disrupting temporal correlations.
- **Training phase**: Trainer workers access these experiences to update the model's weights. This cyclical process allows the model to continuously learn from its actions, adjusting its strategies over time to enhance performance.

The **central master** serves as the central conductor, managing the flow of data and communication between the rollout workers, trainer workers, evaluation with reward models and the replay buffer [p. 9].

The trainer workers access rollout trajectories to compute gradient updates that refine the model's parameters. This process is overseen by a **reward model**, which evaluates the quality of the model's outputs and provides essential feedback to guide the training process [p. 9].

The system incorporates a **code execution service**, specifically designed to handle code-related problems and integral to the reward model. This service evaluates the model's outputs in practical coding scenarios, ensuring that the model's learning is closely aligned with real-world programming challenges [p. 9].

## 2.6.2 Partial Rollouts for Long CoT RL [p. 9]

One of the primary ideas of the work is to scale long-context RL training. Partial rollouts is a key technique that effectively addresses the challenge of handling long-CoT features by managing the rollouts of both long and short trajectories [p. 9]:

- Establishes a **fixed output token budget**, capping the length of each rollout trajectory
- If a trajectory exceeds the token limit during the rollout phase, the **unfinished portion is saved to the replay buffer** and continued in the next iteration
- Ensures that no single lengthy trajectory monopolizes the system's resources
- Rollout workers operate **asynchronously**: when some are engaged with long trajectories, others can independently process new, shorter rollout tasks

As illustrated in Figure 3b, the partial rollout system works by breaking down long responses into segments across iterations (from iter n-m to iter n) [p. 9]:
- The **Replay Buffer** acts as a central storage mechanism that maintains response segments
- Only the **current iteration** (iter n) requires on-policy computation
- **Previous segments** (iter n-m to n-1) can be efficiently reused from the buffer, eliminating the need for repeated rollouts
- During training, certain segments can be **excluded from loss computation** to further optimize the learning process

The implementation also offers **repeat detection**: the system identifies repeated sequences in the generated content and terminates them early, reducing unnecessary computation. Detected repetitions can be assigned additional penalties, effectively discouraging redundant content generation [p. 9].

## 2.6.3 Hybrid Deployment of Training and Inference [p. 9-11]

The RL training process comprises the following phases [p. 9-10]:

- **Training Phase**: Megatron (Shoeybi et al. 2020) and vLLM (Kwon et al. 2023) are executed within separate containers, encapsulated by a shim process known as checkpoint-engine (Section 2.6.3). Megatron commences the training procedure. After training is completed, Megatron offloads the GPU memory and prepares to transfer current weights to vLLM.
- **Inference Phase**: Following Megatron's offloading, vLLM starts with dummy model weights and updates them with the latest ones transferred from Megatron via Mooncake (Qin et al. 2024). Upon completion of the rollout, the checkpoint-engine halts all vLLM processes.
- **Subsequent Training Phase**: Once the memory allocated to vLLM is released, Megatron onloads the memory and initiates another round of training.

**Figure 4** (p. 10): "Hybrid Deployment Framework"

Description: Architecture diagram showing the pod-level deployment with two sidecars
- Key elements: A single pod contains a Megatron Sidecar and a vLLM Sidecar. The Megatron side shows the flow: Train → Offload → Wait rollout → Onload → (repeat). The vLLM side shows: Start vLLM → Update Weight → Terminate Rollout → Terminate vLLM. Both sides communicate through Shared Memory. A Checkpoint Engine manages lifecycle operations. An etcd service provides global metadata, and RDMA connects to Other Pods for checkpoint transfer.
- Notable patterns: The hybrid deployment achieves less than one minute from training to inference phase and about ten seconds conversely [p. 10]
- Supports claim: Efficient resource sharing between training and inference on the same GPUs

The existing works are found challenging to simultaneously support all the following characteristics [p. 10]:
- **Complex parallelism strategy**: Megatron may have different parallelism strategy with vLLM. Training weights distributing in several nodes in Megatron could be challenging to share with vLLM.
- **Minimizing idle GPU resources**: For On-Policy RL, recent works such as SGLang (L. Zheng et al. 2024) and vLLM might reserve some GPUs during the training process, which conversely could lead to idle training GPUs. It would be more efficient to share the same devices between training and inference.
- **Capability of dynamic scaling**: In some cases, a significant acceleration can be achieved by increasing the number of inference nodes while keeping the training process constant. The system enables the efficient utilization of idle GPU nodes when needed.

**Hybrid Deployment Strategy** [p. 10]: A hybrid deployment strategy for training and inference tasks leverages Kubernetes Sidecar containers sharing all available GPUs to collocate both workloads in one pod. Primary advantages:
- Facilitates efficient resource sharing and management, preventing train nodes idling while waiting for inference nodes
- Leveraging distinct deployed images, training and inference can each iterate independently for better performance
- The architecture is not limited to vLLM; other frameworks can be conveniently integrated

**Checkpoint Engine** [p. 10]: Responsible for managing the lifecycle of the vLLM process, exposing HTTP APIs that enable triggering various operations on vLLM. For overall consistency and reliability, a global metadata system managed by the etcd service is used to broadcast operations and statuses.
