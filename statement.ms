Device
 and (hasComponent some 
    (Controller
     and (((observes some ControllerMode)
     and (observes some Execution)) or (hasComponent some 
        (Path
         and (observes some ControllerMode)
         and (observes some Execution))))))



         
