# 075 Sample 

The 075 represent the ligand length of the perovskite material . In this repository sub-folder, we have the [075_sample.csv](https://github.com/alexinthewonderland/Finding-Trap-Densities/blob/main/075-sample/075_sample.csv) and [075_newsample.csv](https://github.com/alexinthewonderland/Finding-Trap-Densities/blob/main/075-sample/075_newsample.csv) file that contains the measurement using a Time Resolved Photoluminescence measurement result. From this measurement, we use the following equation

<p align ="center">
  $\ n_c (t=0) = \Sigma_i n_{TP}^{i} (0) \dot (1-e^{-a_i \tau_0 \frac{I_{PL}}{k}})+ \frac{I_{PL}}{k}$
  </p>

in which $\ n_{TP}^i (0)$ is the $\ i$-th type of trap density when time $\ t$ amounts to zero, $\ a_i$ is the trapping cross section times the carrier velocity, $\ \tau_0$ is the lifetime of the PL decay, and $\ k$ is a constant.

Here, we mostly do an educated guess wok to fit the equation above to the plot of Time interated Photoluminescence Intensity (Time PL) vs Carrier density to obtain the initial traps density value.

# How to use the code
1. By running the second block of code on [075-sample.ipynb](https://github.com/alexinthewonderland/Finding-Trap-Densities/blob/main/075-sample/075-sample.ipynb), you insert the csv file name that contains the Time PL vs Carrier density plot, in this case, it is either ```075_sample.csv``` or the ```075_newsample.csv``` file.
2. Running it would give you the predicted value of the $\ b = a \bullet \tau_0$ and $\ k$ using the ```scipy.optimize.curve_fit``` function but only with a single trap term of the fitted function.
3. Having the value of the constants $\ b$ and $\ k$, we would now add another trap term to obtain a much better fitted result. This is where the third block of code comes to play.
4. Do the same as step 1 and step 2, however, the fitted function here now uses the value of $\ k$ that we have obtained before while using two trap density summation.
5. Then, an educated trial and error is used to find the correct value of $\ b_1$ and $\ b_2$ of the two types of trap density.
6. Finally, the two trap densities are obtained in which we call one as the slow trap and the other as the fast trap.

