https://pythontutor.com/visualize.html#code=recursionDepth%20%3D%202%0Adef%20f1%28var1%29%3A%0A%20%20%20%20print%28%22Entering%20f1%22%29%0A%20%20%20%20f2%28%29%0A%20%20%20%20print%28%22Leaving%20f1%22%29%0A%0Adef%20f2%28%29%3A%0A%20%20%20%20var2%20%3D%2030%0A%20%20%20%20print%28%22Entering%20f2%22%29%0A%20%20%20%20f3%28%29%0A%20%20%20%20print%28%22Leaving%20f2%22%29%0A%0Adef%20f3%28%29%3A%0A%20%20%20%20var3%20%3D%2040%0A%20%20%20%20print%28%22Entering%20f3%22%29%0A%20%20%20%20f4%28%29%0A%20%20%20%20print%28%22Leaving%20f3%22%29%0A%0Adef%20f4%28%29%3A%0A%20%20%20%20var4%20%3D%2050%0A%20%20%20%20print%28%22Entering%20f4%22%29%0A%20%20%20%20global%20recursionDepth%20%0A%20%20%20%20print%28%29%0A%20%20%20%20if%20recursionDepth%20!%3D%201%3A%0A%20%20%20%20%20%20%20%20recursionDepth%20%3D%20recursionDepth%20-%201%0A%20%20%20%20%20%20%20%20f1%2877%29%0A%20%20%20%20%20%20%20%0A%20%20%20%20print%28%22Leaving%20f4%22%29%0A%0Aif%20__name__%20%3D%3D%20'__main__'%3A%0A%20%20%20%20f1%2820%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false