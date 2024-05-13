describe('Demo  Web App Test', () => {
  
  it('Start page successfully loads', () => {
    cy.visit('/')
  });


  it('Application connected to MongoDB', () => {
    const rightContent = 'MongoDB Server Info';
    cy.visit('/db');
    cy.get('body').should('contain', rightContent);
  });
  
});
