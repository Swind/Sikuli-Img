class MultiScaleTemplateMatcher:
    def __init__(self, source_img, target_img):
        self.source_img = source_img.gray()
        self.target_img = target_img.gray()

                
