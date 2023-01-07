import copy
import random
# Consider using the modules imported above.


import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for color, count in kwargs.items():
      self.contents.extend([color] * count)

  def draw(self, num):
    if num >= len(self.contents):
      picked = self.contents
      self.contents = []
      return picked

    draw_order = random.sample(self.contents, len(self.contents))
    self.contents = draw_order[num:]
    return draw_order[:num]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  matches = 0

  for i in range(num_experiments):
    matched = True
    picked = copy.deepcopy(hat).draw(num_balls_drawn)

    for key, value in expected_balls.items():
      if picked.count(key) < value:
        matched = False
        break

    if matched:
      matches += 1
  


  probability = matches / num_experiments

  return probability
