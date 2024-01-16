from envoke import envoke

# Create a macro sequence
sequence = envoke()
sequence.a(interval=0.5).b(.25).c().key('1', interval=.5).key('2', .25).key('3')

# Run the macro
sequence.run(start_delay=2)