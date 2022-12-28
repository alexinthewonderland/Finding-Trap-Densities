{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "from scipy.optimize import curve_fit\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Insert the file name: DDA_sample\n",
      "[  0.98779729 342.64508632 754.69890798]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Reading the file of the data\n",
    "input_filename = input(\"Insert the file name: \")\n",
    "data  = pd.read_csv(\"{0}.csv\".format(input_filename))\n",
    "\n",
    "#Assinging the function and variables\n",
    "def func(x, trap_density, b,k):\n",
    "    #return (trap_density*(1-np.exp(-1*constant*x)))\n",
    "    return (((trap_density*10**15)*(1-np.exp(-1*b*x/k))))\n",
    "\n",
    "# yData = data.carrier_density\n",
    "# for i in range(20):\n",
    "#     yData[i] = yData[i]*10**17\n",
    "\n",
    "yData = data.carrier_density\n",
    "xData = data.time_pl\n",
    "xFit = data.time_pl\n",
    "\n",
    "#Normalizing the x-axis\n",
    "for i in range(5):\n",
    "    xData[i] = xData[i]/xData[4]\n",
    "    \n",
    "xFit = xData\n",
    "\n",
    "\n",
    "#Plotting the Data\n",
    "plt.plot(xData, yData, 'bo', label = \"experimental-data\" )\n",
    "plt.xlabel(\"Time-Integrated PL Intensity (arbs. unit)\")\n",
    "plt.ylabel(\"Carrier Density (cm^-3)\")\n",
    "\n",
    "# if input_filename == \"first_sample\":\n",
    "#     plt.legend([\"PV: Cl-0\", \"Fitted Line\"])\n",
    "# elif input_filename == \"second_sample\":\n",
    "#     plt.legend([\"PV: Cl-0.5\", \"Fitted Line\"])\n",
    "# elif input_filename == \"third_sample\":\n",
    "#     plt.legend([\"PV: Cl-1\", \"Fitted Line\"])\n",
    "    \n",
    "plt.yscale(\"log\") #Assign the y-scale to become a log scale\n",
    "#plt.xscale(\"log\")\n",
    "\n",
    "#Fitting the Data\n",
    "popt, pcov = curve_fit(func, xData, yData) #intial guesses can be written after the yData\n",
    "plt.plot(xFit, func(xFit, *popt), 'r')\n",
    "\n",
    "#Outputting the fitted Trap and Constant Values\n",
    "# for i in range(2):\n",
    "#     if (i == 0):\n",
    "#         print(\"This is the trap density value: \" + str(popt[i]))\n",
    "#     else:\n",
    "#         print(\"This is the constant value: \"+ str(popt[i]))\n",
    "\n",
    "print(popt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Insert the file name: DDA_sample\n",
      "[ 0.99896115 -4.9875074 ]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Reading the file of the data\n",
    "input_filename = input(\"Insert the file name: \")\n",
    "data  = pd.read_csv(\"{0}.csv\".format(input_filename))\n",
    "\n",
    "#Assinging the function and variables\n",
    "def func(x, slowtrap,fasttrap):\n",
    "    #return (trap_density*(1-np.exp(-1*constant*x)))\n",
    "    return (((slowtrap*10**15)*(1-np.exp(-1*342.64508632*x/754.69890798)))+((fasttrap*10**15)*(1-np.exp(-1*0.83757224*x/754.69890798)))+(x/754.69890798)*10**15)\n",
    "\n",
    "# yData = data.carrier_density\n",
    "# for i in range(20):\n",
    "#     yData[i] = yData[i]*10**17\n",
    "\n",
    "yData = data.carrier_density\n",
    "xData = data.time_pl\n",
    "xFit = data.time_pl\n",
    "\n",
    "#Normalizing the x-axis\n",
    "for i in range(5):\n",
    "    xData[i] = xData[i]/xData[4]\n",
    "    \n",
    "xFit = xData\n",
    "\n",
    "\n",
    "#Plotting the Data\n",
    "plt.plot(xData, yData, 'bo', label = \"experimental-data\" )\n",
    "plt.xlabel(\"Time-Integrated PL Intensity (arbs. unit)\")\n",
    "plt.ylabel(\"Carrier Density (cm^-3)\")\n",
    "\n",
    "# if input_filename == \"first_sample\":\n",
    "#     plt.legend([\"PV: Cl-0\", \"Fitted Line\"])\n",
    "# elif input_filename == \"second_sample\":\n",
    "#     plt.legend([\"PV: Cl-0.5\", \"Fitted Line\"])\n",
    "# elif input_filename == \"third_sample\":\n",
    "#     plt.legend([\"PV: Cl-1\", \"Fitted Line\"])\n",
    "    \n",
    "plt.yscale(\"log\") #Assign the y-scale to become a log scale\n",
    "plt.xscale(\"log\")\n",
    "\n",
    "#Fitting the Data\n",
    "popt, pcov = curve_fit(func, xData, yData) #intial guesses can be written after the yData\n",
    "plt.plot(xFit, func(xFit, *popt), 'r')\n",
    "\n",
    "#Outputting the fitted Trap and Constant Values\n",
    "# for i in range(2):\n",
    "#     if (i == 0):\n",
    "#         print(\"This is the trap density value: \" + str(popt[i]))\n",
    "#     else:\n",
    "#         print(\"This is the constant value: \"+ str(popt[i]))\n",
    "\n",
    "print(popt)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
