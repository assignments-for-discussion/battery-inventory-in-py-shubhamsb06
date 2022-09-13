
def count_batteries_by_usage(cycles):
  #create a dictionary to store values for each count
  count_dictionary={"lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
        }
  for cycle in cycles:
    if (cycle<0):
      continue
    elif(cycle<400):
      count_dictionary["lowCount"]+=1
    elif(cycle<920):
      count_dictionary["mediumCount"]+=1
    else:
      count_dictionary["highCount"]+=1
  return count_dictionary


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([-1,-2,100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
