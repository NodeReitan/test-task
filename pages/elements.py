class Elements(object):
    def __init__(self, elements):
        self.elements = elements

    @property
    def compare_size(self):
        if len(self.elements) == 0:
            return False
        first_element = self.elements[0].size
        for element in self.elements:
            if element.size != first_element:
                return False
        return True

    @property
    def get_text_elements(self):
        return list(map(lambda x: x.text, self.elements))
