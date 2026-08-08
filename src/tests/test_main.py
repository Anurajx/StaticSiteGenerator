from main import extract_heading
import unittest


class testMainFunction(unittest.TestCase):
    def testHeadingExtraction(self):
        markdown= """# Tolkien Fan Club

        ![JRR Tolkien sitting](/images/tolkien.png)

        Here's the deal, **I like Tolkien**.

        > "I am in fact a Hobbit in all but size."
        >
        > -- J.R.R. Tolkien """
        
        heading =  extract_heading(markdown)
        #print(heading)
        self.assertEqual(heading,"Tolkien Fan Club")
        
        
    def testMultipleHeadingExtraction(self):
        markdown= """# Tolkien Fan Club
# Matrix Fan Club
        ![JRR Tolkien sitting](/images/tolkien.png)

        Here's the deal, **I like Tolkien**.

        > "I am in fact a Hobbit in all but size."
        >
        > -- J.R.R. Tolkien """
        
        heading =  extract_heading(markdown)
        #print(heading)
        self.assertEqual(heading,"Tolkien Fan Club")
        
    
        
