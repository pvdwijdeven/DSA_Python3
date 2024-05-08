from collections import namedtuple


def create_namedtuple_cls(cls_name, fields):
    return namedtuple(cls_name, fields, rename=True)


import codewars_test as test
from collections import namedtuple, defaultdict
import traceback


def test_namedtuple_creation(cls_name, entries):
    passed = True
    try:
        _cls = create_namedtuple_cls(cls_name, tuple(p[0] for p in entries))
        if _cls.__name__ != cls_name:
            passed = False
            test.assert_equals(_cls.__name__, cls_name)
        if _cls._fields != tuple(p[0] for p in entries):
            passed = False
            test.assert_equals(_cls._fields, tuple(p[0] for p in entries))
        if _cls.__getattribute__ != tuple.__getattribute__:
            passed = False
            test.fail("No metaprogramming! __getattribute__ should be intact")
        if _cls.__getitem__ != tuple.__getitem__:
            passed = False
            test.fail("No metaprogramming! __getitem__ should be intact")

        # ensure returned class is a namedtuple
        instance = tuple.__new__(_cls, (p[1] for p in entries))

        # should not contain extra attributes
        extra_attrs = list(
            set(attr for attr in dir(instance) if not attr.startswith("_"))
            - set(dir(tuple))
        )
        if len(extra_attrs) != len([p[0] for p in entries]):
            passed = False
            test.fail(
                f"namedtuple contains extra attributes!: {extra_attrs} is not equal to {[p[0] for p in entries]}"
            )

        # test attribute access
        for k, v in entries:
            actual = eval(f"instance.{k}")
            if actual != v:
                passed = False
                test.assert_equals(actual, v)

        # test dict access via ._asdict()
        instance_dict = instance._asdict()
        for k, v in entries:
            actual = instance_dict[k]
            if actual != v:
                passed = False
                test.assert_equals(actual, v)

        # test getattr access
        for k, v in entries:
            actual = getattr(instance, k)
            if actual != v:
                passed = False
                test.assert_equals(actual, v)

        test.expect(passed, f"Overall namedtuple test failed")
    except Exception:
        test.fail(
            f"An exception is thrown during attribute access test:\n{traceback.format_exc()}"
        )


@test.describe("Sample Tests")
def sample_tests():
    entries = [
        ("pc", 3.08567758149137e16),
        ("AU", 149597870700),
        ("km", 10**3),
        ("mm", 10**-3),
        ("µm", 10**-6),
        ("nm", 10**-9),
    ]
    cls_name = "LENGTH_UNITS"

    @test.it(f"Testing for\nclass name: {cls_name}\nproperties: {entries}")
    def _():
        test_namedtuple_creation(cls_name, entries)
