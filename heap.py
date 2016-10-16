############################################################################################################################################
# File                          : heap.py                                                                                                  #
# Function                      : Dynamic memory allocation emulation                                                                      #
# Institute                     : MEC                                                                                                      #
############################################################################################################################################

#The memory class.
#Creates a memory array of requested size. 
#Allows dynamic memory allocation on the allocated memory block
import copy


class heap():
    #Constructor function. Accepts the total memory size as input
    #Inputs : 
    #        self : object reference
    #        size : size of the requested memory
    def __init__(self,size):                 
        self.size = size                     #Set the total memory size as whatever is requested by the user
        self.free_mem_assign = size                 #Set total number of nodes
        self.occupied = {}                   #The key to the dictionaries is the block start address and the value is the block end address
        self.mem_assign = []                        
        #Initialize the memory array
        for i in range(1,size+1):              #Initialize the memory contents with zero. zero indicates free 1 occupied
            self.mem_assign.append(0)
        
    #Memory allocation function. Allocates one block size
    #Inputs :
    #       self      : Object reference
    #Returns :
    #       Handle to the block : On success 
    #       -1                  : On failure
    def malloc(self):
        for i in range(1,len(self.mem_assign)):
            if self.mem_assign[i] == 0:
                self.mem_assign[i] = 1
                self.occupied[i] = 0
                return i
        return -1        
        
    #Memory free function. Frees the memory location
    #Inputs :
    #       self      : Object reference
    #       handle    : Handle to the memory block
    #Returns :
    #        0        : On success 
    #       -1        : On failure    
    def free(self,handle):
        try:
            self.mem_assign[handle] = 0
            del(self.occupied[handle])
            return 0
        except:
             return -1
             
    #Copy a cell to the memory
    #Inputs :
    #       self      : Object reference
    #       handle    : Handle to the memory block
    #Returns :
    #        0        : On success 
    #       -1        : On failure             
    def set_cell(self,handle,cell):
        if self.mem_assign[handle] == 1:          #Check whether that handle was previously allocated
            self.occupied[handle]  = copy.copy(cell) #Copy the cell to the memory.
            return 0
        else:
            return -1                      #That handle was not previously allocated
    
    #Retrieve a cell from the memory
    #Inputs :
    #       self      : Object reference
    #       handle    : Handle to the memory block
    #Returns :
    #        cell content        : On success 
    #       -1                   : On failure                 
    def get_cell(self,handle):
        if self.mem_assign[handle] == 1:          #Check whether that handle was previously allocated
            return self.occupied[handle]
        else:
            return -1                      #That handle was not previously allocated
