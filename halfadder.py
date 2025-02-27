import logiclib as lgc #

class HalfAdder(lgc.Circuit): ...

circuit = HalfAdder()

circuit.add_block(lgc.INPUT_PIN, 0,0)
circuit.add_block(lgc.INPUT_PIN, 1,0)
circuit.add_block(lgc.XOR, 0,1)
circuit.add_block(lgc.AND, 1,1)
circuit.add_block(lgc.OUTPUT_PIN, 0,2)
circuit.add_block(lgc.OUTPUT_PIN, 1,2)

grid = circuit.color_visualize()
print(grid, '\n')
print(circuit.to_cm2_save())