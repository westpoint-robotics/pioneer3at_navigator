define vlp16 ranger
(
  sensor
  (
    range_max 30.0
    fov 360.0
   
    samples 1440
  )
  # generic model properties
  color "grey"
  size [ 0.06 0.15 0.03 ]
)

define pioneer_base position 
(
  color "red"     # Default color.
  drive "diff"      # Differential steering model.
  gui_nose 1                    # Draw a nose on the robot so we can see which way it points
  obstacle_return 1             # Can hit things.
  laser_return 1                 # reflects laser beams
  ranger_return 1               # reflects sonar beams
  #blob_return 1                 # Seen by blobfinders  
  #fiducial_return 1             # Seen as "1" fiducial finders

  origin [-0.04465 0.0 0.0 0]
  #localization "gps"            
  #localization_origin [0 0 0 0]   # Start odometry at (0, 0, 0).

  # alternative odometric localization with simple error model
  # localization "odom"             # Change to "gps" to have impossibly perfect, global odometry
  #  odom_error [ 0.05 0.05 0.1 ]     # Odometry error or slip in X, Y and Theta
                                    # (Uniform random distribution)   
)

# The Pioneer3AT standard configuration
define p3at pioneer_base
(
  # Actual size
  size [0.626 0.505 .22]

  # The pioneer's center of rotation is offset from its center of area
  origin [-0.04465 0.0 0.0 0.0]

  # Estimated mass in KG
  mass 40.0 

  # Body shape:
  block( 
    points 8
    point[0] [-0.18 0.313]
    point[1] [0.18 0.313]
    point[2] [0.2525 0.18]
    point[3] [0.2525 -0.18]
    point[4] [0.18 -0.313]
    point[5] [-0.18 -0.313]
    point[6] [-0.2525 -0.18]
    point[7] [-0.2525 0.18]
    z [0 1]
  )


  vlp16(pose [ 0.17 0.0 0.18 0.0 ])
)

define p3at2 position
(
  pose [ 0.0 0.0 0.0 0.0 ]

  odom_error [0.03 0.03 999999 999999 999999 0.02]

  #size [ 0.2552 0.2552 0.40 ]
  origin [ 0.0 0.0 0.0 0.0 ]
  gui_nose 1
  drive "diff"
  color "gray"
  
  size [0.626 0.505 .22]
  # Body shape:
    block( 
    points 8
    point[0] [-0.18 0.313]
    point[1] [0.18 0.313]
    point[2] [0.2525 0.18]
    point[3] [0.2525 -0.18]
    point[4] [0.18 -0.313]
    point[5] [-0.18 -0.313]
    point[6] [-0.2525 -0.18]
    point[7] [-0.2525 0.18]
    z [0 1]
  )

  
  vlp16(pose [ -0.1 0.0 -0.11 0.0 ])
)
