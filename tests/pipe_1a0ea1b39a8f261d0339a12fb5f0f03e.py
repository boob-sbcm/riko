# Pipe pipe_1a0ea1b39a8f261d0339a12fb5f0f03e generated by pipe2py

from pipe2py.modules import pipeitembuilder, pipedateformat, pipeinput


def pipe_1a0ea1b39a8f261d0339a12fb5f0f03e(item=None, context=None, conf=None, **kwargs):
    conf = conf or {}

    if context and context.describe_input:
        return []

    if context and context.describe_dependencies:
        return [u'pipedatebuilder', u'pipedateformat', u'pipeitembuilder']

    sw_385 = pipe_datebuilder(
        context=context, conf={'DATE': {'type': 'datetime', 'value': '12/2/2014'}})

    sw_405 = pipe_dateformat(
        sw_385, context=context, conf={
            'timezone': {'type': 'text', 'value': ''},
            'format': {'type': 'text', 'value': '%B %d, %Y'}})

    sw_393 = pipe_itembuilder(
        item,
        context=context,
        conf={
            'attrs': [
                        {
                            'value': {'terminal': 'attrs_1_value', 'type': 'text'},
                            'key': {'type': 'text', 'value': 'date'}
                        }, {
                            'value': {'value': '1201', 'type': 'text'},
                            'key': {'type': 'text', 'value': 'year'}}]},
        attrs_1_value=sw_405,
        **kwargs)

    return sw_393


if __name__ == "__main__":
    pipeline = pipe_1a0ea1b39a8f261d0339a12fb5f0f03e()

    for i in pipeline:
        print i