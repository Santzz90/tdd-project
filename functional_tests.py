# Quando ela aperta enter, a página atualiza, e mostra a lista
        # "1: Estudar testes funcionais" como um item da lista TODO
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        
        # ---> MUDE ESTA PARTE <---
        self.assertTrue(
            any(row.text == '1: Estudar testes funcionais' for row in rows),
            "New to-do item did not appear in table"
        )