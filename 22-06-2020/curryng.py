def a(arg1):
    print(arg1)
    def b(arg2):
        print(arg2)
        def c(arg3):
            print(arg3)
            def d(arg4):
                print(11, arg1, arg2, arg3, arg4)
            return d
        return c
    return b

# obj_b = a(123)
# obj_c = obj_b(321)
# obj_d = obj_c(456)
# obj_d(999)
a(123)(321)(456)(999)