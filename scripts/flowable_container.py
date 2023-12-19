FLOWABLE_CONTAINER_WIDTHS = []

flowable_container = document.getElementById("flowable-container")
for i in flowable_container.children:
    FLOWABLE_CONTAINER_WIDTHS.append(i.style.width)

def render_flowable_container():
    flowable_container = document.getElementById("flowable-container")
    space_available = flowable_container.clientWidth
    
