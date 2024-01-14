from conjure import conjure

# Create a macro sequence
sequence = conjure(start_delay=2)
sequence.enter(interval=0.5).key('a', interval=0.1)

# Run the macro
sequence.run()
