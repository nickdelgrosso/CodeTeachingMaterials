#version 330 core

attribute vec4 vertexPosition;

uniform mat4 model_matrix = mat4(1.0);
uniform mat4 view_matrix = mat4(1.0);
uniform mat4 projection_matrix = mat4(vec4(1.38564062,  0.,  0.,  0.),
                                      vec4(0.,  1.73205078,  0.,  0.),
                                      vec4(0., 0., -1.01680672, -1. ),
                                      vec4(0., 0., -0.20168068, 0.)
                                      );

void main()
  {
    //Calculate Vertex Position on Screen
	gl_Position = projection_matrix * view_matrix * model_matrix * vertexPosition;

//      gl_Position = view_matrix * model_matrix * vertexPosition;
  }
