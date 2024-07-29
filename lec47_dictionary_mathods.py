ep1={
    122:45,123:89,221:90,342:67
}
ep2={222:67,566:90

}
ep1.update(ep2)
print(ep1)
# ep1.clear()
ep1.pop(122)
ep1.popitem()  #removes the last item of the dict
print(ep1)
# del ep1
