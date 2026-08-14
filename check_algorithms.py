"""Plain if/else PASS/FAIL checks for the TaskFlow algorithms."""

from backend.algorithms import (
    binary_search,
    binary_search_count,
    insertion_sort,
    insertion_sort_count,
    linear_search,
    linear_search_count,
)


def check(name: str, condition: bool) -> None:
    if condition:
        print(f"PASS: {name}")
    else:
        print(f"FAIL: {name}")


def main() -> None:
    numbers = [5, 2, 4, 1, 3]

    sorted_numbers = insertion_sort(
        numbers,
        key=lambda value: value,
    )

    check(
        "insertion_sort sorts ascending",
        sorted_numbers == [1, 2, 3, 4, 5],
    )

    check(
        "insertion_sort does not mutate input",
        numbers == [5, 2, 4, 1, 3],
    )

    found_binary = binary_search(
        sorted_numbers,
        4,
        key=lambda value: value,
    )

    check(
        "binary_search finds existing value",
        found_binary == 4,
    )

    missing_binary = binary_search(
        sorted_numbers,
        99,
        key=lambda value: value,
    )

    check(
        "binary_search returns None for missing value",
        missing_binary is None,
    )

    found_linear = linear_search(
        numbers,
        2,
        key=lambda value: value,
    )

    check(
        "linear_search finds existing value",
        found_linear == 2,
    )

    missing_linear = linear_search(
        numbers,
        99,
        key=lambda value: value,
    )

    check(
        "linear_search returns None for missing value",
        missing_linear is None,
    )

    counted_sort, sort_counter = insertion_sort_count(
        numbers,
        key=lambda value: value,
    )

    check(
        "insertion_sort_count produces correct result",
        counted_sort == [1, 2, 3, 4, 5],
    )

    check(
        "insertion_sort_count records operations",
        sort_counter.total > 0,
    )

    counted_binary, binary_counter = binary_search_count(
        sorted_numbers,
        3,
        key=lambda value: value,
    )

    check(
        "binary_search_count finds target",
        counted_binary == 3,
    )

    check(
        "binary_search_count records operations",
        binary_counter.total > 0,
    )

    counted_linear, linear_counter = linear_search_count(
        numbers,
        5,
        key=lambda value: value,
    )

    check(
        "linear_search_count finds target",
        counted_linear == 5,
    )

    check(
        "linear_search_count records operations",
        linear_counter.total > 0,
    )

    print("\nAlgorithm checks complete.")


if __name__ == "__main__":
    main()