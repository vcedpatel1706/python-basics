Question : what is need of this we can calculate time by putting time() before and after of example_function

                start = time.time()
                example_function(3)
                end = time.time()
                print(f"Function ran in {end - start} seconds")

✅ Decorator is useful when:
1. **You want to reuse the timing logic for many functions.**
   Instead of repeating `start = time.time()` and `end = time.time()` everywhere,
   you can just add `@timer` above the function — clean and reusable.
2. **You don’t want to modify the original function.**

   Suppose `example_function()` is written by someone else or in a different file.
   You don't want to edit its code — so you "wrap" it with a decorator like `@timer`.

