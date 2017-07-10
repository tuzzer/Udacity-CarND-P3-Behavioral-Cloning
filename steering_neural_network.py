from keras.models import Sequential
from keras.layers import Flatten, Dense, Conv2D, MaxPooling2D, Dropout
from keras.optimizers import Adam


class SteeringNeuralNetwork():

    def __init__(self, input_shape, output_shape):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.model = self.create_network(input_shape, output_shape)

    @staticmethod
    def create_network(input_shape, output_shape):
        activation = "relu"

        model = Sequential()
        model.add(Conv2D(16, (3, 3), strides=(2, 2), name="convolution0", padding='same', activation=activation, input_shape=input_shape))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(32, (3, 3), strides=(2, 2), activation=activation, padding='same', name="convolution1"))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(64, (3, 3), activation=activation, padding='same', name="convolution2"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dropout(0.5))

        model.add(Dense(100, activation=activation, name="dense0"))
        model.add(Dropout(0.5))

        model.add(Dense(50, activation=activation, name="dense1"))
        model.add(Dropout(0.5))

        model.add(Dense(10, activation=activation, name="dense2"))
        model.add(Dropout(0.5))

        model.add(Dense(output_shape, name="output"))

        adam = Adam(lr=1e-04, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
        model.compile(optimizer=adam, loss="mse")

        return model