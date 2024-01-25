class HtmlTag:
    def __init__(self, tag, body=None):
        self.tag = tag
        self.classes = []
        self.attributes = {}
        self.id = ""
        self.body = body or ""
        self.children = []

    def add_class(self, class_name: str):
        self.classes.append(class_name)

        return self

    def add_attribute(self, attr_name: str, attr_value: str):
        self.attributes[attr_name] = attr_value

        return self

    def add_child(self, child):
        self.children.append(child)

        return self

    def add_children(self, children: list):
        self.children.extend(children)

        return self

    def set_body(self, body: str):
        self.body = body

        return self

    def set_id(self, id: str):
        self.id = id

        return self

    def partial_render(self) -> str:
        attributes = []

        if self.id:
            attributes.append(f'id="{self.id}"')

        if self.classes:
            attributes.append(f'class="{", ".join(self.classes)}"')

        for attr_name, attr_value in self.attributes.items():
            attributes.append(f'{attr_name}="{attr_value}"')

        final_attributes = ""

        if attributes:
            final_attributes = " " + " ".join(attributes)
        else:
            final_attributes = ""

        return f"<{self.tag}{final_attributes}>"

    def render(self) -> str:
        partial = self.partial_render()

        if self.children:
            children = "".join([str(child) for child in self.children])
            return f"{partial}{children}</{self.tag}>"

        return f"{partial}{self.body}</{self.tag}>"

    def __str__(self) -> str:
        return self.render()
