import numpy as np
np.set_printoptions(precision=2)
import matplotlib.pyplot as plt

from matplotlib.ticker import FuncFormatter

#
### Function to calculatie the value function given the initial value
#


H_ix = 0 #hardcode indices for H and T
T_ix = 1

def calculate_distribution_HH(t_max = 100): #time to caluclate up to


  x_max = t_max #the maximum absolute x value we need to calculate too in time t_max

  # x ranges from 0 to +x_max inclusive
  probs = np.zeros((t_max+1,x_max+1,2)) #probability be be at state when started from (0,T)

  t,x,coins = np.indices((t_max+1,x_max+1,2))

  probs[0,0,H_ix] = 0.0
  probs[0,0,T_ix] = 1.0


  for t in range(1,t_max+1):
    for ix in range(x_max+1):

      if ix == 0:
        probs[t,0,H_ix] = 0 + 0.5*probs[t-1,0,T_ix]
        probs[t,0,T_ix] = 0.5*probs[t-1,0,H_ix] + 0.5*probs[t-1,0,T_ix]
      elif ix > 0:
        probs[t,ix,H_ix] = 0.5*probs[t-1,ix-1,H_ix] + 0.5*probs[t-1,ix,T_ix]
        probs[t,ix,T_ix] = 0.5*probs[t-1,ix,H_ix] + 0.5*probs[t-1,ix,T_ix]

  return probs


def calculate_distribution_HT(t_max = 100): #time to caluclate up to
  x_max = t_max #the maximum absolute x value we need to calculate too in time t_max

  # x ranges from 0 to +x_max inclusive
  probs = np.zeros((t_max+1,x_max+1,2)) #probability be be at state when started from (0,T)

  t,x,coins = np.indices((t_max+1,x_max+1,2))

  probs[0,0,H_ix] = 0.0
  probs[0,0,T_ix] = 1.0


  for t in range(1,t_max+1):
    for ix in range(x_max+1):

      if ix == 0:
        probs[t,0,H_ix] = 0.5*probs[t-1,0,H_ix] + 0.5*probs[t-1,0,T_ix]
        probs[t,0,T_ix] = 0 + 0.5*probs[t-1,0,T_ix]
      elif ix > 0:
        probs[t,ix,H_ix] = 0.5*probs[t-1,ix,H_ix] + 0.5*probs[t-1,ix,T_ix]
        probs[t,ix,T_ix] = 0.5*probs[t-1,ix-1,H_ix] + 0.5*probs[t-1,ix,T_ix]

  return probs


def calculate_distribution_HH_plus_TT(t_max = 100): #time to caluclate up to
  x_max = t_max #the maximum absolute x value we need to calculate too in time t_max

  # x ranges from 0 to +x_max inclusive
  probs = np.zeros((t_max+1,x_max+1,2)) #probability be be at state when started from (0,T)

  t,x,coins = np.indices((t_max+1,x_max+1,2))

  probs[0,0,H_ix] = 0.0
  probs[0,0,T_ix] = 1.0


  for t in range(1,t_max+1):
    for ix in range(x_max+1):

      if ix == 0:
        probs[t,0,H_ix] = 0.0*probs[t-1,0,H_ix] + 0.5*probs[t-1,0,T_ix]
        probs[t,0,T_ix] = 0.5*probs[t-1,0,H_ix] + 0.0*probs[t-1,0,T_ix]
      elif ix > 0:
        probs[t,ix,H_ix] = 0.5*probs[t-1,ix-1,H_ix] + 0.5*probs[t-1,ix,T_ix]
        probs[t,ix,T_ix] = 0.5*probs[t-1,ix,H_ix] + 0.5*probs[t-1,ix-1,T_ix]

  return probs

def calculate_distribution_HT_plus_TT(t_max = 100): #time to caluclate up to
  x_max = t_max #the maximum absolute x value we need to calculate too in time t_max

  # x ranges from 0 to +x_max inclusive
  probs = np.zeros((t_max+1,x_max+1,2)) #probability be be at state when started from (0,T)

  t,x,coins = np.indices((t_max+1,x_max+1,2))

  probs[0,0,H_ix] = 0.0
  probs[0,0,T_ix] = 1.0


  for t in range(1,t_max+1):
    for ix in range(x_max+1):

      if ix == 0:
        probs[t,0,H_ix] = 0.5*probs[t-1,0,H_ix] + 0.5*probs[t-1,0,T_ix]
        probs[t,0,T_ix] = 0.0*probs[t-1,0,H_ix] + 0.0*probs[t-1,0,T_ix]
      elif ix > 0:
        probs[t,ix,H_ix] = 0.5*probs[t-1,ix,H_ix] + 0.5*probs[t-1,ix,T_ix]
        probs[t,ix,T_ix] = 0.5*probs[t-1,ix-1,H_ix] + 0.5*probs[t-1,ix-1,T_ix]

  return probs

t_max = 100



H_color = r'#118ab2' #;"cornflowerblue"
T_color = r'#ffd166' #"gold"
Tie_color = r'#06d6a0' #'springgreen'
Adv_color = r'#ef476f' #coral'
plt.style.use('dark_background')

alice = calculate_distribution_HH(t_max)
prob_HH = alice[t_max,:,H_ix] + alice[t_max,:,T_ix]
print(np.sum(prob_HH))


bob = calculate_distribution_HT(t_max)
prob_HT = bob[t_max,:,H_ix] + bob[t_max,:,T_ix]
print(np.sum(prob_HT))

alice_modified = calculate_distribution_HH_plus_TT(t_max)
prob_HH_plus_TT = alice_modified[t_max,:,H_ix] + alice_modified[t_max,:,T_ix]
print(np.sum(prob_HH_plus_TT))

bob_modified = calculate_distribution_HT_plus_TT(t_max)
prob_HT_plus_TT = bob_modified[t_max,:,H_ix] + bob_modified[t_max,:,T_ix]
print(np.sum(prob_HT_plus_TT))


for frame in range(2):

  fig, ax = plt.subplots(figsize=(8, 8))
  # Plotting a bar chart
  ax.bar(np.arange(t_max+1),prob_HH,alpha=1.0,label=f"Number of HH (Alice)", color=H_color)
  ax.bar(np.arange(t_max+1),prob_HT,alpha=0.6,label=f"Number of HT (Bob)",color=T_color)
  if frame >= 1:
    ax.bar(np.arange(t_max+1),prob_HH_plus_TT,alpha=1.0,label=f"Number of HH plus TT",hatch='..',color=H_color)
    ax.bar(np.arange(t_max+1),prob_HT_plus_TT,alpha=0.6,label=f"Number of HT plus TT",hatch=r'..',color=T_color)


  my_fontsize = 20# Increase the size of major ticks
  # Set labels and title with increased font size
  ax.set_xlabel('Score', fontsize=my_fontsize)  # Adjust the font size as needed
  ax.set_ylabel('Probability', fontsize=my_fontsize)  # Adjust the font size as needed
  ax.set_title(f'Distribution of individual scores in {t_max} flips \n (i.e. indirect competion)', fontsize=my_fontsize)   # Adjust the font size as needed

  # Customize axis limits and ticks
  #ax.set_xticks(np.arange(len(data)))  # Set the positions of x-axis ticks
  #ax.set_xticklabels(['A', 'B', 'C', 'D', 'E'])  # Set the labels for x-axis ticks
  #ax.set_ylim(0, max(data) + 10)  # Adjust the y-axis limits to ensure all bars are visible

  ax.tick_params(axis='both', which='major', labelsize=14)  # Adjust the size as needed, also can adjust the font size

  ax.legend(fontsize=my_fontsize*1.05)

  # Add grid

  ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{100*y:.0f}%'))
  ax.grid(axis='y',linestyle='--')

  # Adjust layout
  fig.tight_layout()

  # Display the plot
  plt.show()
