def clip_output_to_interval(a, b):
    def clip_output_of_f(f):
        def new_f(*args):
            output = f(*args)

            clipped_output = tuple(map(lambda xi: max(a, min(b, xi)), output))

            return clipped_output

        return new_f

    return clip_output_of_f
