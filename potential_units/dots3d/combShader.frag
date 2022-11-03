#version 330 core

uniform vec3 diffuse;

void main()
{
//    gl_FragColor = vec4(clamp(diffuse, 0, 1), 1.0);
    gl_FragColor = vec4(1., 1., 1., 1.);
 }
