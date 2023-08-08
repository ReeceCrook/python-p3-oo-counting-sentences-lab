#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value=''):
    self.value = value

  def get_value(self):
    return self._value

  def set_value(self, value):
    if (type(value) == str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    if(self.value.endswith(".")):
      return True
    else:
      return False
    
  def is_question(self):
    if(self.value.endswith("?")):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if(self.value.endswith("!")):
      return True
    else:
      return False
    
  def count_sentences(self):
    split_string = []
    count = 0
    split_string.append(re.split('[!|?|.]', self.value))
    for i in range(len(split_string[0])):
      if len(split_string[0][i]) != 0:
        count += 1

    return count
    
  value = property(get_value, set_value)
