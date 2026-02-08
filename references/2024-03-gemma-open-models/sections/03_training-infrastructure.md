# Training Infrastructure [p. 3]

The Gemma models are trained using TPUv5e. TPUv5e are deployed in pods of 256 chips, configured into a 2D torus of 16 x 16 chips. [p. 3]

- **7B model:** trained across 16 pods, totaling 4096 TPUv5e. Within a pod, 16-way model sharding and 16-way data replication are used.
- **2B model:** pretrained across 2 pods, totaling 512 TPUv5e. Within a pod, 256-way data replication is used.

The optimizer state is further sharded using techniques similar to ZeRO-3. Beyond a pod, data-replica reduce is performed over the data-center network, using the Pathways approach of (Barham et al., 2022). [p. 3]

The authors follow Gemini and leverage the 'single controller' programming paradigm of Jax (Roberts et al., 2023) and Pathways (Barham et al., 2022). This simplifies the development process by enabling a single Python process to orchestrate the entire training run. The GSPMD partitioner (Xu et al., 2021) is leveraged for the training step computation and the MegaScale XLA compiler (XLA, 2019). [p. 3]

## Carbon Footprint

The estimated carbon emissions from pretraining the Gemma models is ~131 tCO2eq. This value is calculated based on the hourly energy usage reported directly from the TPU datacenters; it is also scaled to account for the additional energy expended to create and maintain the data center, giving the total energy usage for training experiments. Total energy usage is converted to carbon emissions by joining hourly energy usage against hourly per-cell carbon emission data reported by the data centers. [p. 3]

Google data centers are carbon neutral, achieved through a combination of energy efficiency, renewable energy purchases, and carbon offsets. This carbon neutrality applies to their experiments and the machines running them. [p. 3]
