for start_index in range(len(gas)):
            # print(f"start index : {start_index}")
            
            gas_store = gas[start_index]
            use_cost = cost[start_index]
            jump_index = start_index

            while True:
                jump_index = (jump_index+1) if (jump_index + 1) < len(gas) else 0
                # print(f"jump to index: {jump_index}")
                gas_store -= use_cost
                if gas_store < 0:
                    break
                
                gas_store += gas[jump_index] 
                use_cost = cost[jump_index]

                if jump_index == start_index:
                    gas_store -= use_cost
                    if gas_store >= 0:
                        return start_index
    
                    break