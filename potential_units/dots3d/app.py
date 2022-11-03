from psychopy import visual, event
import numpy as np
import ratcave as rc
from ratcave.vertex import VAO, VBO

win = visual.Window()

shader = rc.Shader.from_file("combShader.vert", "combShader.frag")

verts = np.hstack((
    np.random.random((9999, 3)).astype(np.float32) * 2 - 1,
    np.ones((9999, 1)).astype(np.float32)
))
vbo = VBO(verts)
vao = VAO()
vao.assign_vertex_attrib_location(vbo, 0)



camera = rc.Camera(projection=rc.PerspectiveProjection(z_far=2, z_near=0.01))
camera.position.x = 0.2

rc.mesh.gl.glPointSize(5.)
camera.uniforms.pop('model_matrix')
while 'escape' not in event.getKeys():
    camera.position.z -= 0.05
    # print(camera.view_matrix)

    with shader, camera:
        print(camera.uniforms)

        rc.clear_color(0, 0, 0.2)
        # verts[:, :3] = np.random.random((999, 3)) * 2 - 1
        # vbo._buffer_subdata()
        vao.draw(mode=rc.POINTS)
        win.flip()