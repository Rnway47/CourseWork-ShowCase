#please run this on Jhub since hmm module cannot be installed on the uvic linux server
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from hmmlearn import hmm

def plot_samples(samples, state2color, title): 
    colors = [state2color[x] for x in samples]
    x = np.arange(0, len(colors))
    y = np.ones(len(colors))
    plt.figure(figsize=(10,1))
    plt.bar(x, y, color=colors, width=1)
    plt.title(title)

transmat = np.array([[0.63, 0.37], #CGD, CGS
                    [0.37, 0.63]]) #CGS
start_prob = np.array([0.5, 0.5])
emission_probs = ([0.15, 0.35, 0.35, 0.15], #A C G T
                  [0.4, 0.1, 0.1, 0.4])

model = hmm.CategoricalHMM(n_components=2) #switch to categorical HMM, check the output message once it's generated
model.startprob_ = start_prob 
model.transmat_ = transmat 
model.emissionprob_ = emission_probs
 
X, Z = model.sample(1000) #1000 samples, X stands for observed states, and Z stands for hidden states

# we have to re-define state2color and obj2color as the hmm-learn 
# package just outputs numbers for the states 
state2color = {} 
state2color[0] = 'black' # CGD 
state2color[1] = 'white' # CGS
plot_samples(Z, state2color, 'states')

samples = [item for sublist in X for item in sublist]
obj2color = {} 
obj2color[0] = 'red' # A
obj2color[1] = 'green' # C
obj2color[2] = 'blue' # T
obj2color[3] = 'yellow' # G
plot_samples(samples, obj2color, 'observations')
plt.show()

# generate the samples 
X, Z = model.sample(10000)
# learn a new model 
estimated_model = hmm.CategoricalHMM(n_components=2, n_iter=10000).fit(X)

print("Transition matrix")
print("Estimated model:")
print(estimated_model.transmat_)
print("Original model:")
print(model.transmat_)
print("Emission probabilities")
print("Estimated model")
print(estimated_model.emissionprob_)
print("Original model")
print(model.emissionprob_)