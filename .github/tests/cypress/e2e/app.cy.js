describe('Demo  Web App Test', () => {
  
  it('Start page successfully loads', () => {
    cy.visit('/')
  });

  it('Start page shows right content', () => {
    const rightContent = 'Permission for data processing';
    cy.visit('/');
    cy.get('body').should('contain', rightContent);
  });

  it('Application connected to MongoDB', () => {
    const rightContent = 'MongoDB Server Info';
    cy.visit('/db');
    cy.get('body').should('contain', rightContent);
  });
  
});
