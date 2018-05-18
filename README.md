# Convert Channels

This code was built to convert a .h5 content from one shape to other.
More specifically, it changed a conv1 group from (7, 7, 3, 64) to (7, 7, 20, 64)
in order to train a UCF101 dataset using imagenet as a start point. 

## Usage

First of all, change the parameters inside, like folder name and new_shape.

$ python3 convert_channel.py

## References

* https://arxiv.org/abs/1507.02159


