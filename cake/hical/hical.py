def sort_meetings(meetings):
    """Sorts meetings by start time. Not implemented."""
    return meetings


def merge_meetings(meetings):
    sorted_meetings = sort_meetings(meetings)
    meeting_count = len(sorted_meetings)

    if meeting_count < 2:
        return meetings

    start, stop = 0, 1
    min_start, max_stop = None, None
    result = []

    for i in range(meeting_count-1):
        no_more_meetings = (i + 1) == (meeting_count - 1)
        current_meeting = sorted_meetings[i]
        next_meeting = sorted_meetings[i+1]

        if min_start == None:
            min_start = current_meeting[start]

        if max_stop == None:
            max_stop = current_meeting[stop]

        if max_stop >= next_meeting[start]:
            # Next meeting could still end before current meeting.
            max_stop = max(max_stop, next_meeting[stop])

        if current_meeting[stop] < next_meeting[start] or no_more_meetings:
            result.append((min_start, max_stop))
            min_start, max_stop = None, None

    return result


if __name__ == "__main__":
    # Sorting meetings is not implemented, so order here.
    print merge_meetings([(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)])
    print merge_meetings([(1, 3), (2, 4)])
    print merge_meetings([(1, 10), (2, 6), (3, 5), (7, 9)])
