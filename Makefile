create-practice:
ifdef PRACTICE
	$(error must pass val PRACTICE)
	
endif
	@echo "Creating practice"
	mkdir -p $(PRACTICE)

remove-practice:
ifdef PRACTICE
	$(error must pass val PRACTICE)
	
endif
	rm -rf $(PRACTICE)
help:
	@echo "This makefile for repo.level activity"

#mkdir demo-practice
#mkdir demo-practice/src
#mkdir demo-practice/tests
#mkdir demo-practice/docs
#mkdir demo-practice/README.md