all: commands-summary.md

clean:
	rm -f commands-summary.md

commands-summary.md: commands.md scripts/commands_create_summary.py
	./scripts/commands_create_summary.py commands.md commands-summary.md

.PHONY: all clean
