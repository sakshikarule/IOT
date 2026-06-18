# range
#   sequence data type - collection / sequence of value
#   can be used in loop or to create another collection (list or tuple)
#   sequence is not stored in range object, it is generated at run time when requested


#   range(stop)              - create a sequence from 0 to stop-1
#   range(start, stop)       - create a sequence from start to stop-1
#   range(start, stop, step) - create q sequence from start to stop-1, increment by step

# for val in range(10):             # 0-9
# for val in range(11, 20):         # 11-19
# for val in range(11, 20, 2):        # 11 13 15 17 19
#    print(val)               


seq = range(10)
print(f"type(seq) = {type(seq)}")
print(f"seq = {seq}")
for val in seq:
    print(val)