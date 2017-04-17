from make_training_data import makeTrainingData, LearningPlayer
from count_wins import countWins
from game import Player, Game
from bad_player import BadPlayer
from human_player import play

import numpy as np
import tensorflow as tf

predict = None

class NeuralNetworkPlayer(LearningPlayer):
    def chooseHandIndex(self, discard, score):
        inputVector = self.getInputVector(discard, score)
        global predict
        output = predict(inputVector)

        handIndex, option = self.getChoiceFromOutput(output)

        return handIndex, option

def main():
  # mostly copied from https://www.tensorflow.org/get_started/tflearn
  # Load datasets.
  training_input, training_output = makeTrainingData(1000, 3)
  test_input, test_output = makeTrainingData(20, 3)

  print training_input, training_output

  # Specify that all features have real-value data
  feature_columns = [tf.contrib.layers.real_valued_column("", dimension=53)]

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                              hidden_units=[10, 20, 10],
                                              n_classes=6,
                                              model_dir="/tmp/card99_model")
  # Define the training inputs
  def get_train_inputs():
    x = tf.constant(training_input)
    y = tf.constant(training_output)

    return x, y

  # Fit model.
  classifier.fit(input_fn=get_train_inputs, steps=len(training_input))

  # Define the test inputs
  def get_test_inputs():
    x = tf.constant(test_input)
    y = tf.constant(test_output)

    return x, y

  # Evaluate accuracy.
  accuracy_score = classifier.evaluate(input_fn=get_test_inputs,
                                       steps=1)["accuracy"]

  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

  def predictFunc(inputVector):
      def new_samples():
          return np.array(
            [inputVector], dtype=np.float32)

      c = list(classifier.predict(input_fn=new_samples))
      print c
      return c[0];

  global predict
  predict = predictFunc


  #play(NeuralNetworkPlayer(1))
  countWins(150, [Player, Player, NeuralNetworkPlayer])


if __name__ == "__main__":
    main()
