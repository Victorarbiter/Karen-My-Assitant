print ("\nHello my name is Karen, nice to meet you")
print  ("This is my neural network test")
print ("=============================================")

from numpy import exp, array, random, dot
class NeuralNetwork():
    def __init__(self):
        random.seed(1)
        self.synaptic_weights = 2 * random.random((3, 1)) - 1
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # trial and error.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(10000):
            output = self.think(training_set_inputs)
            # Menghitung error
            error = training_set_outputs - output
            # Mengkali nilai error dengan input.
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment

    #  Neural network .
    def think(self, inputs):
        #  single neuron
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":

    #Mengintegrasi neuran dengan neural network.
    neural_network = NeuralNetwork()

    print ("\nRandom starting synaptic weights: ")
    print (neural_network.synaptic_weights)

    # Matriks 3x1 sebagai test input
    # 1 matriks 4x1 sebagai output .
    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T

    # latihan neural network
    # melakukan 10000 kali dengan pendekan sebanyak 10000
    neural_network.train(training_set_inputs, training_set_outputs, 20000)

    print ("\nNew synaptic weights after training: ")
    print (neural_network.synaptic_weights)

    # Hasil dari neural network.
    print ("\nConsidering new situation [1, 0, 0] -> ?: ")
    print ( neural_network.think(array([1, 0, 0])))
    # Jika hasilnya mendekati 1 maka, neural network berjalan dengan baik
if neural_network.think(array([1, 0, 0])) >= [0.755] :
   print ("\nIt's working perfectly Sir")

if neural_network.think(array([1, 0, 0])) <= [0.755] :
   print ("\nIt's something went wrong")
