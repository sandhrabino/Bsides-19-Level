import sys
import angr
import claripy

def main(argv):
  path_to_binary = argv[1]
  project = angr.Project(path_to_binary)
  print_good_address = 0x00000400786 
  #will_not_succeed_address = 0x000000400C61
  
  arg_char=[claripy.BVS('flag_%d' % i,8) for i in range(20)]
  arg=claripy.Concat(*arg_char+[claripy.BVV(b'\n')])
  
  initial_state = project.factory.full_init_state(args='./level',add_options=angr.options.unicorn,stdin=arg)
  
  for i in arg_char:
      initial_state.solver.add(i>=0x20)
      initial_state.solver.add(i<=0x7e)
      
    
  simulation = project.factory.simgr(initial_state)
  simulation.explore(find=print_good_address)
  
  if simulation.found:
    solution_state = simulation.found[0]
    print(solution_state.posix.dumps(sys.stdin.fileno()))
  else :
      print('No!')
if __name__ == '__main__':
  main(sys.argv)


