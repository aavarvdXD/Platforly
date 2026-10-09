import pygame as pg

class ParallaxLayer:
    def __init__(self, img, depth):
        self.img = img
        self.depth = depth
        self.width = img.get_width()

    def render(self, surf, offset=(0, 0)):
        # Calculate the horizontal shift based on camera offset and depth
        # For standard parallax, shift = offset * depth
        # We use modulo to wrap the image
        x_shift = -(offset[0] * self.depth) % self.width
        
        # Draw two copies to handle wrapping
        surf.blit(self.img, (x_shift, 0))
        surf.blit(self.img, (x_shift - self.width, 0))

class Clouds:
    def __init__(self, cloudImgs, size):
        self.layers = []
        for i, img in enumerate(cloudImgs):
            # Scale image to screen size as requested in previous steps
            scaled_img = pg.transform.scale(img, size)

            depth = (i + 1) * 0.2
            self.layers.append(ParallaxLayer(scaled_img, depth))
            
        self.layers.sort(key=lambda x: x.depth)

    def update(self):
        # In this standard parallax implementation, movement is driven by camera offset in render()
        pass

    def render(self, surf, offset=(0, 0)):
        for layer in self.layers:
            layer.render(surf, offset=offset)