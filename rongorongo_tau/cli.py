"""Rongorongo Tau — CLI entry point."""

import argparse
from .navigator import lookup, list_tablets, trace_variation


def main():
    parser = argparse.ArgumentParser(description='Rongorongo Tau — ritual formula variation tracker')
    sub = parser.add_subparsers(dest='command')

    p_lookup = sub.add_parser('lookup', help='Look up a glyph family')
    p_lookup.add_argument('code', help='Barthel glyph code (e.g. G001)')

    p_list = sub.add_parser('list', help='List all tablets')

    p_trace = sub.add_parser('trace', help='Trace variation across a glyph sequence')
    p_trace.add_argument('glyphs', nargs='+', help='Glyph codes in sequence')

    args = parser.parse_args()

    if args.command == 'lookup':
        result = lookup(args.code)
        print(f"Glyph {result['glyph_code']}: {result['description']}")
        print(f"  Tuple: {''.join(result['tuple'])}")
        print(f"  In core cycle: {result['in_core_cycle']}")

    elif args.command == 'list':
        tablets = list_tablets()
        for t in tablets:
            print(f"{t['label']:40s}  {''.join(t['tuple'])}")

    elif args.command == 'trace':
        result = trace_variation(args.glyphs)
        print(f"Sequence: {' '.join(result['sequence'])}")
        print(f"Glyphs: {result['glyph_count']}")
        print(f"Core cycle participation: {result['core_cycle_hits']}/{result['glyph_count']}")
        print(f"Cycle fraction: {result['core_cycle_fraction']:.2f}")
        print(f"Boustrophedon: {result['boustrophedon_flip']}")
        for g in result['glyph_details']:
            print(f"  {g['glyph_code']}: {g.get('description','')}")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
