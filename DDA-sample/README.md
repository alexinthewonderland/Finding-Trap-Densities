# DDA Sample

Dodecylammonium or DDA is a long chain ammonium cation which is added to the ligand of the 2D perovskite that we would like to study the trap density. In this repository sub-folder, we have the [DDA_sample.csv](https://github.com/alexinthewonderland/Finding-Trap-Densities/blob/main/DDA-sample/DDA_sample.csv) file that contains the measurement using a Time Resolved Photoluminescence measurement result. From this measurement, we use the following equation

<p align ="center">
  $\ n_c (t=0) = \Sigma_i n_{TP}^{i} (0) \dot (1-e^{-a_i \tau_0 \frac{I_{PL}}{k}})+ \frac{I_{PL}}{k}$
  </p>

in which $\ n_{TP}^i (0)$ is the 𝑖th type of trap density when time $\ (t)$ amounts to zero, $\ a_i $ is the trapping cross section times the carrier velocity, $\ \tau_0 $ is the lifetime of the PL decay, and $\ k$ is a constant.

Here, we mostly do an educated guess wok to fit the equation above to the plot of Time PL vs Carrier density to obtain the initial traps density value.

# Understanding the code
